# RDS PostgreSQL 数据库配置

# 数据库子网组
resource "aws_db_subnet_group" "main" {
  name       = "${var.cluster_name}-db-subnet"
  subnet_ids = module.vpc.database_subnets

  tags = {
    Name = "${var.cluster_name}-db-subnet-group"
  }
}

# 数据库安全组
resource "aws_security_group" "rds" {
  name_prefix = "${var.cluster_name}-rds-"
  description = "Security group for RDS PostgreSQL"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description = "PostgreSQL from EKS"
    from_port   = 5432
    to_port     = 5432
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
    Name = "${var.cluster_name}-rds-sg"
  }
}

# RDS 参数组
resource "aws_db_parameter_group" "main" {
  name_prefix = "${var.cluster_name}-postgres-"
  family      = "postgres16"

  parameter {
    name  = "log_connections"
    value = "1"
  }

  parameter {
    name  = "log_disconnections"
    value = "1"
  }

  parameter {
    name  = "log_statement"
    value = "all"
  }

  parameter {
    name  = "shared_preload_libraries"
    value = "pg_stat_statements"
  }

  tags = {
    Name = "${var.cluster_name}-postgres-params"
  }
}

# RDS 实例
resource "aws_db_instance" "main" {
  identifier     = "${var.cluster_name}-postgres"
  engine         = "postgres"
  engine_version = "16.1"
  instance_class = var.rds_instance_class

  allocated_storage     = var.rds_allocated_storage
  max_allocated_storage = var.rds_allocated_storage * 2
  storage_type          = "gp3"
  storage_encrypted     = true

  db_name  = "{{ cookiecutter.database_name }}"
  username = "{{ cookiecutter.database_user }}"
  password = random_password.db_password.result

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  parameter_group_name   = aws_db_parameter_group.main.name

  # 备份配置
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "mon:04:00-mon:05:00"

  # 高可用性
  multi_az               = true
  publicly_accessible    = false
  deletion_protection    = true
  skip_final_snapshot    = false
  final_snapshot_identifier = "${var.cluster_name}-final-snapshot-${formatdate("YYYY-MM-DD-hhmm", timestamp())}"

  # 性能洞察
  performance_insights_enabled    = true
  performance_insights_retention_period = 7

  # 自动次要版本升级
  auto_minor_version_upgrade = true

  tags = {
    Name = "${var.cluster_name}-postgres"
  }
}

# 数据库密码
resource "random_password" "db_password" {
  length  = 32
  special = true
}

# 将密码存储到 AWS Secrets Manager
resource "aws_secretsmanager_secret" "db_password" {
  name_prefix = "${var.cluster_name}-db-password-"
  description = "Database password for {{ cookiecutter.project_name }}"

  recovery_window_in_days = 7
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({
    username = aws_db_instance.main.username
    password = random_password.db_password.result
    engine   = "postgres"
    host     = aws_db_instance.main.address
    port     = aws_db_instance.main.port
    dbname   = aws_db_instance.main.db_name
    url      = "postgresql://${aws_db_instance.main.username}:${random_password.db_password.result}@${aws_db_instance.main.address}:${aws_db_instance.main.port}/${aws_db_instance.main.db_name}"
  })
}

