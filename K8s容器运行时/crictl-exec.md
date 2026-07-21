---
{
  "cmd_name": "crictl exec",
  "cmd_category": "Kubernetes Container Runtime",
  "cmd_dimension": "Kubernetes Container Runtime",
  "cmd_install": "Download from https://github.com/kubernetes-sigs/cri-tools/releases",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-runtime.yaml"
}
---

# crictl exec

> Execute command in running container

## 安装

```bash
Download from https://github.com/kubernetes-sigs/cri-tools/releases
```

## 用法

```
crictl exec [flags] [container-id] [command]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | Keep STDIN open |
| `-t` | Allocate a pseudo-TTY |

## 示例

### 示例 1: Execute ls command in container

```bash
crictl exec <container-id> ls /
```

### 示例 2: Open interactive shell in container

```bash
crictl exec -it <container-id> /bin/sh
```

### 示例 3: Show environment variables in container

```bash
crictl exec <container-id> env
```

## 风险提示

> ⚠️ **HIGH**: Can execute arbitrary commands in running containers

## 所属维度

[[K8s容器运行时-MOC|Kubernetes Container Runtime]]
