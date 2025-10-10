# 部署手册

本文档详细说明如何将 {{ cookiecutter.project_name }} 部署到生产环境。

## 📋 目录

1. [部署架构](#部署架构)
2. [前置准备](#前置准备)
3. [Docker 部署](#docker-部署)
4. [Kubernetes 部署](#kubernetes-部署)
5. [云平台部署](#云平台部署)
6. [监控和日志](#监控和日志)
7. [备份和恢复](#备份和恢复)
8. [故障排查](#故障排查)

## 🏗️ 部署架构

```
┌─────────────────────────────────────────────────────────────┐
│                        Cloudflare CDN                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────────┐
│                    Kubernetes Cluster                        │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Frontend   │  │   Backend    │  │   ML API     │      │
│  │    (Nuxt)    │  │  (FastAPI)   │  │  (YOLOv8)    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │               │
│         └──────────────────┴──────────────────┘              │
│                            │                                  │
│  ┌─────────────────────────┴────────────────────────┐       │
│  │              Traefik Ingress Controller          │       │
│  └──────────────────────────────────────────────────┘       │
└───────────────────────────────────────────────────────────── │

┌───────────────────────────────────────────────────────────┐
│                    Infrastructure                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │PostgreSQL│  │  Redis   │  │  MinIO   │  │  Jaeger  │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘ │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │Prometheus│  │ Grafana  │  │   Loki   │               │
│  └──────────┘  └──────────┘  └──────────┘               │
└───────────────────────────────────────────────────────────┘
```

## 🔑 前置准备

### 1. 域名和 DNS 配置

```bash
# 在 Cloudflare 中添加 DNS 记录
{{ cookiecutter.domain_name }}         A      <your-server-ip>
api.{{ cookiecutter.domain_name }}    A      <your-server-ip>
*.{{ cookiecutter.domain_name }}      A      <your-server-ip>
```

### 2. SSL 证书

使用 cert-manager 自动获取 Let's Encrypt 证书：

```bash
# 安装 cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml

# 创建 ClusterIssuer
kubectl apply -f infra/kubernetes/core-infra/cert-manager/cluster-issuer.yaml
```

### 3. 密钥管理

```bash
# 创建 Kubernetes secrets

# 数据库密钥
kubectl create secret generic postgres-secret \
  --from-literal=password='<your-db-password>' \
  -n {{ cookiecutter.kubernetes_namespace }}

# JWT 密钥
kubectl create secret generic jwt-secret \
  --from-literal=secret-key='<your-jwt-secret>' \
  -n {{ cookiecutter.kubernetes_namespace }}

# S3 密钥
kubectl create secret generic s3-credentials \
  --from-literal=access-key='<your-access-key>' \
  --from-literal=secret-key='<your-secret-key>' \
  -n {{ cookiecutter.kubernetes_namespace }}

# 镜像拉取密钥
kubectl create secret docker-registry regcred \
  --docker-server={{ cookiecutter.docker_registry }} \
  --docker-username=<username> \
  --docker-password=<password> \
  -n {{ cookiecutter.kubernetes_namespace }}
```

## 🐳 Docker 部署

### 1. 构建镜像

```bash
# 构建所有镜像
docker-compose build

# 或分别构建
docker build -t {{ cookiecutter.project_slug }}-backend:latest ./services/backend
docker build -t {{ cookiecutter.project_slug }}-frontend:latest ./services/frontend
{% if cookiecutter.enable_ml_api == 'yes' -%}
docker build -t {{ cookiecutter.project_slug }}-ml-api:latest ./services/ml-api
{% endif -%}
```

### 2. 推送到镜像仓库

```bash
# 登录镜像仓库
docker login {{ cookiecutter.docker_registry }}

# 标记镜像
docker tag {{ cookiecutter.project_slug }}-backend:latest {{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-backend:latest
docker tag {{ cookiecutter.project_slug }}-frontend:latest {{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-frontend:latest

# 推送镜像
docker push {{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-backend:latest
docker push {{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-frontend:latest
```

### 3. 使用 Docker Compose 部署

```bash
# 创建生产环境配置
cp docker-compose.yml docker-compose.prod.yml

# 编辑生产配置
nano docker-compose.prod.yml

# 启动服务
docker-compose -f docker-compose.prod.yml up -d

# 查看状态
docker-compose -f docker-compose.prod.yml ps

# 查看日志
docker-compose -f docker-compose.prod.yml logs -f
```

## ☸️ Kubernetes 部署

### 1. 准备 Kubernetes 集群

```bash
# 使用 kubeadm (自建集群)
kubeadm init --pod-network-cidr=10.244.0.0/16

# 或使用云服务提供商
# AWS EKS, Google GKE, Azure AKS 等

# 验证集群
kubectl cluster-info
kubectl get nodes
```

### 2. 部署核心基础设施

```bash
# 创建命名空间
kubectl create namespace {{ cookiecutter.kubernetes_namespace }}

# 部署 Traefik Ingress Controller
helm repo add traefik https://traefik.github.io/charts
helm install traefik traefik/traefik \
  --namespace traefik-system \
  --create-namespace \
  -f infra/kubernetes/core-infra/traefik/values.yaml

# 部署 cert-manager
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true

{% if cookiecutter.enable_monitoring == 'yes' -%}
# 部署 Prometheus Operator
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f infra/kubernetes/core-infra/prometheus/values.yaml
{% endif -%}
```

### 3. 部署数据库和缓存

```bash
# 部署 PostgreSQL
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install postgresql bitnami/postgresql \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set auth.username={{ cookiecutter.database_user }} \
  --set auth.password=<your-password> \
  --set auth.database={{ cookiecutter.database_name }} \
  --set primary.persistence.size=20Gi

# 部署 Redis
helm install redis bitnami/redis \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set auth.enabled=false \
  --set master.persistence.size=8Gi

# 部署 MinIO
helm install minio bitnami/minio \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set auth.rootUser=admin \
  --set auth.rootPassword=<your-password> \
  --set defaultBuckets={{ cookiecutter.project_slug }}-uploads \
  --set persistence.size=50Gi
```

### 4. 部署应用服务

```bash
# 部署后端
helm install backend ./infra/kubernetes/helm-charts/backend \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set image.repository={{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-backend \
  --set image.tag=latest \
  --set ingress.host=api.{{ cookiecutter.domain_name }} \
  -f infra/kubernetes/helm-charts/backend/values.prod.yaml

# 部署前端
helm install frontend ./infra/kubernetes/helm-charts/frontend \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set image.repository={{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-frontend \
  --set image.tag=latest \
  --set ingress.host={{ cookiecutter.domain_name }} \
  -f infra/kubernetes/helm-charts/frontend/values.prod.yaml

{% if cookiecutter.enable_ml_api == 'yes' -%}
# 部署 ML API
helm install ml-api ./infra/kubernetes/helm-charts/ml-api \
  --namespace {{ cookiecutter.kubernetes_namespace }} \
  --set image.repository={{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-ml-api \
  --set image.tag=latest \
  -f infra/kubernetes/helm-charts/ml-api/values.prod.yaml
{% endif -%}
```

### 5. 验证部署

```bash
# 查看所有资源
kubectl get all -n {{ cookiecutter.kubernetes_namespace }}

# 查看 Pod 状态
kubectl get pods -n {{ cookiecutter.kubernetes_namespace }} -w

# 查看服务
kubectl get svc -n {{ cookiecutter.kubernetes_namespace }}

# 查看 Ingress
kubectl get ingress -n {{ cookiecutter.kubernetes_namespace }}

# 查看日志
kubectl logs -f deployment/backend -n {{ cookiecutter.kubernetes_namespace }}
```

## 🚀 云平台部署

### AWS 部署

```bash
# 1. 使用 OpenTofu 创建基础设施
cd infra/tofu/environments/production

# 初始化 Tofu
tofu init

# 查看执行计划
tofu plan -out=tfplan

# 应用配置
tofu apply tfplan

# 2. 配置 EKS 集群
aws eks update-kubeconfig --name {{ cookiecutter.project_slug }}-cluster --region us-east-1

# 3. 部署应用
# 按照上述 Kubernetes 部署步骤执行
```

### Google Cloud 部署

```bash
# 1. 创建 GKE 集群
gcloud container clusters create {{ cookiecutter.project_slug }}-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=n1-standard-2

# 2. 获取凭证
gcloud container clusters get-credentials {{ cookiecutter.project_slug }}-cluster \
  --zone=us-central1-a

# 3. 部署应用
# 按照 Kubernetes 部署步骤执行
```

### Azure 部署

```bash
# 1. 创建 AKS 集群
az aks create \
  --resource-group {{ cookiecutter.project_slug }}-rg \
  --name {{ cookiecutter.project_slug }}-cluster \
  --node-count 3 \
  --node-vm-size Standard_DS2_v2 \
  --generate-ssh-keys

# 2. 获取凭证
az aks get-credentials \
  --resource-group {{ cookiecutter.project_slug }}-rg \
  --name {{ cookiecutter.project_slug }}-cluster

# 3. 部署应用
# 按照 Kubernetes 部署步骤执行
```

## 📊 监控和日志

{% if cookiecutter.enable_monitoring == 'yes' -%}
### Prometheus 监控

```bash
# 访问 Prometheus
kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090

# 访问 Grafana
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80

# 默认登录信息
# Username: admin
# Password: prom-operator
```

### 日志收集 (Loki)

```bash
# 部署 Loki
helm repo add grafana https://grafana.github.io/helm-charts
helm install loki grafana/loki-stack \
  --namespace monitoring \
  --set grafana.enabled=false \
  --set prometheus.enabled=false

# 在 Grafana 中添加 Loki 数据源
# URL: http://loki:3100
```

### 分布式追踪 (Jaeger)

```bash
# 部署 Jaeger
kubectl apply -f infra/kubernetes/core-infra/jaeger/jaeger.yaml

# 访问 Jaeger UI
kubectl port-forward -n monitoring svc/jaeger-query 16686:16686
# 打开 http://localhost:16686
```
{% endif -%}

## 💾 备份和恢复

### 数据库备份

```bash
# 手动备份
kubectl exec -it postgresql-0 -n {{ cookiecutter.kubernetes_namespace }} -- \
  pg_dump -U {{ cookiecutter.database_user }} {{ cookiecutter.database_name }} > backup.sql

# 使用脚本自动备份
bash scripts/db-backup.sh

# 恢复数据库
kubectl exec -i postgresql-0 -n {{ cookiecutter.kubernetes_namespace }} -- \
  psql -U {{ cookiecutter.database_user }} {{ cookiecutter.database_name }} < backup.sql
```

### 定时备份 (CronJob)

```yaml
# infra/kubernetes/cronjobs/db-backup.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: postgres-backup
spec:
  schedule: "0 2 * * *"  # 每天凌晨 2 点
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: postgres:16-alpine
            command:
            - /bin/sh
            - -c
            - |
              pg_dump -U {{ cookiecutter.database_user }} {{ cookiecutter.database_name }} | \
              gzip > /backup/backup-$(date +%Y%m%d-%H%M%S).sql.gz
          restartPolicy: OnFailure
```

## 🔧 故障排查

### 查看 Pod 状态

```bash
# 查看 Pod 详情
kubectl describe pod <pod-name> -n {{ cookiecutter.kubernetes_namespace }}

# 查看 Pod 事件
kubectl get events -n {{ cookiecutter.kubernetes_namespace }} --sort-by='.lastTimestamp'

# 查看容器日志
kubectl logs <pod-name> -n {{ cookiecutter.kubernetes_namespace }} --previous
```

### 常见问题

#### Pod 无法启动

```bash
# 检查镜像是否存在
kubectl describe pod <pod-name> -n {{ cookiecutter.kubernetes_namespace }} | grep Image

# 检查资源限制
kubectl top pods -n {{ cookiecutter.kubernetes_namespace }}
kubectl top nodes
```

#### 数据库连接失败

```bash
# 测试数据库连接
kubectl run -it --rm debug --image=postgres:16-alpine --restart=Never -- \
  psql -h postgresql.{{ cookiecutter.kubernetes_namespace }}.svc.cluster.local \
  -U {{ cookiecutter.database_user }} -d {{ cookiecutter.database_name }}
```

#### Ingress 不工作

```bash
# 检查 Ingress 配置
kubectl describe ingress -n {{ cookiecutter.kubernetes_namespace }}

# 检查 Traefik 日志
kubectl logs -n traefik-system -l app.kubernetes.io/name=traefik
```

## 🔄 滚动更新

```bash
# 更新镜像
kubectl set image deployment/backend \
  backend={{ cookiecutter.docker_registry }}/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}-backend:v1.1.0 \
  -n {{ cookiecutter.kubernetes_namespace }}

# 查看滚动更新状态
kubectl rollout status deployment/backend -n {{ cookiecutter.kubernetes_namespace }}

# 回滚到上一个版本
kubectl rollout undo deployment/backend -n {{ cookiecutter.kubernetes_namespace }}

# 查看部署历史
kubectl rollout history deployment/backend -n {{ cookiecutter.kubernetes_namespace }}
```

## 🔒 安全加固

### 网络策略

```yaml
# 限制 Pod 之间的网络访问
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8000
```

### Pod 安全策略

```yaml
# 限制 Pod 权限
apiVersion: policy/v1beta1
kind:PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  runAsUser:
    rule: MustRunAsNonRoot
  fsGroup:
    rule: RunAsAny
  volumes:
  - 'configMap'
  - 'emptyDir'
  - 'secret'
```

## 📈 性能优化

### 水平扩缩容 (HPA)

```bash
# 创建 HPA
kubectl autoscale deployment backend \
  --cpu-percent=70 \
  --min=2 \
  --max=10 \
  -n {{ cookiecutter.kubernetes_namespace }}

# 查看 HPA 状态
kubectl get hpa -n {{ cookiecutter.kubernetes_namespace }}
```

### 垂直扩缩容 (VPA)

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: backend-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: backend
  updatePolicy:
    updateMode: "Auto"
```

## 📚 相关资源

- [Kubernetes 官方文档](https://kubernetes.io/docs/)
- [Helm 文档](https://helm.sh/docs/)
- [Traefik 文档](https://doc.traefik.io/traefik/)
- [Prometheus 文档](https://prometheus.io/docs/)

---

**注意**: 在生产环境部署前，请确保：
1. ✅ 所有密钥已正确配置
2. ✅ 数据库已备份
3. ✅ 监控和告警已设置
4. ✅ 已进行充分测试
5. ✅ 有回滚方案

