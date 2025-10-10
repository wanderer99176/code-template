# ElastiCache Redis 配置

# Redis 子网组
resource "aws_elasticache_subnet_group" "main" {
  name       = "${var.cluster_name}-redis-subnet"
  subnet_ids = module.vpc.private_subnets

  tags = {
    Name = "${var.cluster_name}-redis-subnet-group"
  }
}

# Redis 安全组
resource "aws_security_group" "redis" {
  name_prefix = "${var.cluster_name}-redis-"
  description = "Security group for ElastiCache Redis"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description = "Redis from EKS"
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = module.vpc.private_subnets_cidr_blocks
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.cluster_name}-redis-sg"
  }
}

# Redis 参数组
resource "aws_elasticache_parameter_group" "main" {
  name_prefix = "${var.cluster_name}-redis-"
  family      = "redis7"

  parameter {
    name  = "maxmemory-policy"
    value = "allkeys-lru"
  }

  parameter {
    name  = "timeout"
    value = "300"
  }

  tags = {
    Name = "${var.cluster_name}-redis-params"
  }
}

# Redis 复制组（集群模式）
resource "aws_elasticache_replication_group" "main" {
  replication_group_id       = "${var.cluster_name}-redis"
  replication_group_description = "Redis cluster for {{ cookiecutter.project_name }}"

  engine               = "redis"
  engine_version       = "7.1"
  node_type            = var.elasticache_node_type
  num_cache_clusters   = 2  # 主节点 + 1个副本
  port                 = 6379

  subnet_group_name    = aws_elasticache_subnet_group.main.name
  security_group_ids   = [aws_security_group.redis.id]
  parameter_group_name = aws_elasticache_parameter_group.main.name

  # 高可用性
  automatic_failover_enabled = true
  multi_az_enabled          = true

  # 备份配置
  snapshot_retention_limit = 5
  snapshot_window         = "03:00-05:00"
  maintenance_window      = "sun:05:00-sun:07:00"

  # 加密
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  auth_token                 = random_password.redis_auth_token.result

  # 自动次要版本升级
  auto_minor_version_upgrade = true

  tags = {
    Name = "${var.cluster_name}-redis"
  }
}

# Redis 认证令牌
resource "random_password" "redis_auth_token" {
  length  = 32
  special = false
}

# 将 Redis 配置存储到 Secrets Manager
resource "aws_secretsmanager_secret" "redis_config" {
  name_prefix = "${var.cluster_name}-redis-config-"
  description = "Redis configuration for {{ cookiecutter.project_name }}"

  recovery_window_in_days = 7
}

resource "aws_secretsmanager_secret_version" "redis_config" {
  secret_id = aws_secretsmanager_secret.redis_config.id
  secret_string = jsonencode({
    primary_endpoint = aws_elasticache_replication_group.main.primary_endpoint_address
    reader_endpoint  = aws_elasticache_replication_group.main.reader_endpoint_address
    port            = aws_elasticache_replication_group.main.port
    auth_token      = random_password.redis_auth_token.result
    url             = "rediss://:${random_password.redis_auth_token.result}@${aws_elasticache_replication_group.main.primary_endpoint_address}:${aws_elasticache_replication_group.main.port}/0"
  })
}

