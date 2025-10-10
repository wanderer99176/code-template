# OpenTofu (Terraform) 主配置文件
# 用于在云平台上自动化部署基础设施

terraform {
  required_version = ">= 1.6"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.11"
    }
  }

  # 状态后端配置（使用 S3）
  backend "s3" {
    bucket         = "{{ cookiecutter.project_slug }}-terraform-state"
    key            = "production/terraform.tfstate"
    region         = var.aws_region
    encrypt        = true
    dynamodb_table = "{{ cookiecutter.project_slug }}-terraform-locks"
  }
}

# AWS Provider 配置
provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "{{ cookiecutter.project_name }}"
      Environment = var.environment
      ManagedBy   = "OpenTofu"
    }
  }
}

# Kubernetes Provider 配置
provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
  }
}

# Helm Provider 配置
provider "helm" {
  kubernetes {
    host                   = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
    
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      command     = "aws"
      args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
    }
  }
}

