# OpenTofu (Terraform) 基础设施配置

本目录包含使用 OpenTofu (Terraform) 在 AWS 上自动部署 {{ cookiecutter.project_name }} 的完整基础设施代码。

## 📋 前置条件

1. **安装工具**:
   ```bash
   # 安装 OpenTofu
   brew install opentofu  # macOS
   # 或者
   curl -L https://github.com/opentofu/opentofu/releases/latest/download/tofu_linux_amd64.tar.gz | tar xz
   
   # 安装 AWS CLI
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

2. **配置 AWS 凭证**:
   ```bash
   aws configure
   ```

3. **创建 S3 后端** (首次部署):
   ```bash
   # 创建状态存储桶
   aws s3 mb s3://{{ cookiecutter.project_slug }}-terraform-state --region us-west-2
   
   # 创建锁表
   aws dynamodb create-table \
     --table-name {{ cookiecutter.project_slug }}-terraform-locks \
     --attribute-definitions AttributeName=LockID,AttributeType=S \
     --key-schema AttributeName=LockID,KeyType=HASH \
     --billing-mode PAY_PER_REQUEST \
     --region us-west-2
   ```

## 🚀 部署步骤

### 1. 初始化

```bash
cd infra/tofu
tofu init
```

### 2. 规划变更

```bash
# 查看将要创建的资源
tofu plan

# 将计划保存到文件
tofu plan -out=tfplan
```

### 3. 应用变更

```bash
# 应用保存的计划
tofu apply tfplan

# 或者直接应用
tofu apply
```

### 4. 配置 kubectl

```bash
# 使用输出的命令配置 kubectl
aws eks update-kubeconfig --region us-west-2 --name {{ cookiecutter.project_slug }}-cluster
```

## 📦 创建的资源

### 网络层
- VPC (CIDR: 10.0.0.0/16)
- 3个可用区，每个包含：
  - 公共子网（用于 Load Balancer）
  - 私有子网（用于应用）
  - 数据库子网（用于 RDS）
- NAT 网关（每个可用区一个）
- VPC Endpoints（S3, ECR）

### 计算层
- EKS 集群 (Kubernetes {{ "1.28" }})
- EKS Managed Node Groups:
  - General: 2-10个 t3.large 实例
  {% if cookiecutter.use_gpu == "yes" -%}
  - GPU: 0-5个 g4dn.xlarge 实例
  {% endif -%}
- Cluster Autoscaler
- AWS Load Balancer Controller

### 数据层
- RDS PostgreSQL 16（Multi-AZ）
- ElastiCache Redis 7（集群模式）
- S3 存储桶：
  - 应用数据存储
  - ML 模型存储

### 安全层
- IAM Roles for Service Accounts (IRSA)
- Security Groups
- AWS Secrets Manager（密码管理）
- VPC Endpoints（私有连接）

## 💰 成本估算

基础配置预估月成本（us-west-2）：

| 服务 | 配置 | 月成本（USD） |
|------|------|---------------|
| EKS 集群 | 1个集群 | $73 |
| EC2 (一般节点) | 3 × t3.large | ~$190 |
{% if cookiecutter.use_gpu == "yes" -%}
| EC2 (GPU节点) | 1 × g4dn.xlarge | ~$240 |
{% endif -%}
| RDS PostgreSQL | db.t3.medium (Multi-AZ) | ~$120 |
| ElastiCache Redis | cache.t3.medium × 2 | ~$100 |
| NAT Gateway | 3 × NAT Gateway | ~$100 |
| 数据传输 | 估算 | ~$50 |
| **总计** | | **~${% if cookiecutter.use_gpu == "yes" %}873{% else %}633{% endif %}** |

> **注意**: 这只是基础成本估算，实际成本取决于：
> - 自动扩缩容情况
> - 数据传输量
> - S3 存储和请求
> - CloudWatch 日志

## 🔧 自定义配置

编辑 `variables.tf` 或创建 `terraform.tfvars`:

```hcl
# terraform.tfvars
aws_region = "us-west-2"
environment = "production"

# 节点组配置
node_groups = {
  general = {
    desired_size   = 5
    min_size       = 3
    max_size       = 20
    instance_types = ["t3.xlarge"]
  }
}

# 数据库配置
rds_instance_class = "db.r6g.large"
rds_allocated_storage = 200

# Redis 配置
elasticache_node_type = "cache.r6g.large"
```

## 🔍 查看输出

```bash
# 查看所有输出
tofu output

# 查看特定输出
tofu output cluster_endpoint
tofu output rds_endpoint
```

## 🧹 清理资源

```bash
# 销毁所有资源
tofu destroy

# 销毁特定资源
tofu destroy -target=module.eks
```

## 📚 高级操作

### 导入现有资源

```bash
tofu import aws_s3_bucket.app_data my-existing-bucket
```

### 状态管理

```bash
# 查看状态
tofu state list

# 移动资源
tofu state mv aws_instance.old aws_instance.new

# 删除资源（不销毁实际资源）
tofu state rm aws_instance.example
```

### 多环境管理

```bash
# 使用 workspace
tofu workspace new staging
tofu workspace select production
tofu workspace list
```

## 🔐 安全最佳实践

1. **启用 MFA Delete** 用于 S3 状态桶
2. **加密所有数据**（已在配置中启用）
3. **使用 AWS Secrets Manager** 管理敏感信息
4. **定期轮换密码和密钥**
5. **启用 CloudTrail** 审计
6. **使用 Security Groups** 限制访问
7. **启用 VPC Flow Logs**

## 📖 参考文档

- [OpenTofu 文档](https://opentofu.org/docs/)
- [AWS EKS 最佳实践](https://aws.github.io/aws-eks-best-practices/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

