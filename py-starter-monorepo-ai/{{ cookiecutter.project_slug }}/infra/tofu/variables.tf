# OpenTofu 变量定义

variable "aws_region" {
  description = "AWS 区域"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "环境名称"
  type        = string
  default     = "production"
}

variable "cluster_name" {
  description = "EKS 集群名称"
  type        = string
  default     = "{{ cookiecutter.project_slug }}-cluster"
}

variable "cluster_version" {
  description = "Kubernetes 版本"
  type        = string
  default     = "1.28"
}

variable "vpc_cidr" {
  description = "VPC CIDR 块"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "可用区列表"
  type        = list(string)
  default     = ["us-west-2a", "us-west-2b", "us-west-2c"]
}

variable "node_groups" {
  description = "EKS 节点组配置"
  type = map(object({
    desired_size   = number
    min_size       = number
    max_size       = number
    instance_types = list(string)
  }))
  default = {
    general = {
      desired_size   = 3
      min_size       = 2
      max_size       = 10
      instance_types = ["t3.large"]
    }
    {% if cookiecutter.use_gpu == "yes" %}
    gpu = {
      desired_size   = 1
      min_size       = 0
      max_size       = 5
      instance_types = ["g4dn.xlarge"]
    }
    {% endif %}
  }
}

variable "rds_instance_class" {
  description = "RDS 实例类型"
  type        = string
  default     = "db.t3.medium"
}

variable "rds_allocated_storage" {
  description = "RDS 存储大小 (GB)"
  type        = number
  default     = 100
}

variable "elasticache_node_type" {
  description = "ElastiCache 节点类型"
  type        = string
  default     = "cache.t3.medium"
}

variable "domain_name" {
  description = "域名"
  type        = string
  default     = "{{ cookiecutter.domain_name }}"
}

