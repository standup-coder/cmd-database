---
{
  "cmd_name": "kind",
  "cmd_category": "容器编排/本地K8s",
  "cmd_dimension": "本地K8s",
  "cmd_install": "参考 https://kind.sigs.k8s.io/docs/user/quick-start/#installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "minikube",
    "kubectl"
  ],
  "cmd_tags": [
    "docker",
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/local-k8s.yaml"
}
---

# kind

> 使用 Docker 容器运行本地 Kubernetes 集群

## 安装

```bash
参考 https://kind.sigs.k8s.io/docs/user/quick-start/#installation
```

## 用法

```
kind [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `create cluster` | 创建集群 |
| `delete cluster` | 删除集群 |
| `load docker-image` | 将本地镜像加载到集群节点 |

## 示例

### 示例 1: 创建名为 dev 的本地集群

```bash
kind create cluster --name dev
```

### 示例 2: 将本地镜像加载到 kind 集群

```bash
kind load docker-image myapp:latest --name dev
```

## 关联命令

- [[minikube]]
- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 创建多个集群会占用较多内存和 CPU，请确认本机资源

## 所属维度

[[本地K8s-MOC|容器编排/本地K8s]]
