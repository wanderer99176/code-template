# OpenTofu 输出值

output "cluster_name" {
  description = "EKS 集群名称"
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "EKS 集群 API endpoint"
  value       = module.eks.cluster_endpoint
}

output "cluster_certificate_authority_data" {
  description = "EKS 集群证书"
  value       = module.eks.cluster_certificate_authority_data
  sensitive   = true
}

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "private_subnets" {
  description = "私有子网 IDs"
  value       = module.vpc.private_subnets
}

output "public_subnets" {
  description = "公共子网 IDs"
  value       = module.vpc.public_subnets
}

output "rds_endpoint" {
  description = "RDS PostgreSQL endpoint"
  value       = aws_db_instance.main.endpoint
}

output "rds_connection_string" {
  description = "RDS 连接字符串"
  value       = "postgresql://${aws_db_instance.main.username}:****@${aws_db_instance.main.address}:${aws_db_instance.main.port}/${aws_db_instance.main.db_name}"
}

output "redis_primary_endpoint" {
  description = "Redis 主节点 endpoint"
  value       = aws_elasticache_replication_group.main.primary_endpoint_address
}

output "redis_reader_endpoint" {
  description = "Redis 读节点 endpoint"
  value       = aws_elasticache_replication_group.main.reader_endpoint_address
}

output "s3_app_data_bucket" {
  description = "应用数据 S3 存储桶"
  value       = aws_s3_bucket.app_data.id
}

output "s3_ml_models_bucket" {
  description = "ML 模型 S3 存储桶"
  value       = aws_s3_bucket.ml_models.id
}

output "db_secret_arn" {
  description = "数据库密码 Secrets Manager ARN"
  value       = aws_secretsmanager_secret.db_password.arn
}

output "redis_secret_arn" {
  description = "Redis 配置 Secrets Manager ARN"
  value       = aws_secretsmanager_secret.redis_config.arn
}

# 配置 kubectl 的命令
output "configure_kubectl" {
  description = "配置 kubectl 的命令"
  value       = "aws eks update-kubeconfig --region ${var.aws_region} --name ${module.eks.cluster_name}"
}

