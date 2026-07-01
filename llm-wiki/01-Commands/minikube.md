---
{
  "cmd_name": "minikube",
  "cmd_category": "容器编排/本地K8s",
  "cmd_dimension": "本地K8s",
  "cmd_install": "参考 https://minikube.sigs.k8s.io/docs/start/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "kind"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/local-k8s.yaml"
}
---

# minikube

> 本地单节点 Kubernetes 集群工具

## 安装

```bash
参考 https://minikube.sigs.k8s.io/docs/start/
```

## 用法

```
minikube [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `start` | 启动集群 |
| `stop` | 停止集群 |
| `dashboard` | 打开 Kubernetes 仪表盘 |

## 示例

### 示例 1: 使用 Docker 驱动启动 minikube

```bash
minikube start --driver=docker
```

### 示例 2: 获取服务的访问 URL

```bash
minikube service my-service --url
```

## 关联命令

- [[kubectl]]
- [[kind]]

## 风险提示

> ⚠️ **MEDIUM**: minikube 会创建虚拟机/容器，请确保有足够磁盘和内存

## 所属维度

[[本地K8s-MOC|容器编排/本地K8s]]
