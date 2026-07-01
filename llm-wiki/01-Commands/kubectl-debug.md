---
{
  "cmd_name": "kubectl debug",
  "cmd_category": "Kubernetes Troubleshooting",
  "cmd_dimension": "Kubernetes Troubleshooting",
  "cmd_install": "kubectl 内置命令 (v1.18+)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-troubleshooting.yaml"
}
---

# kubectl debug

> 创建调试容器进行故障排查

## 安装

```bash
kubectl 内置命令 (v1.18+)
```

## 用法

```
kubectl debug [pod-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--image` | 调试容器镜像 |
| `-it` | 交互式调试 |
| `--copy-to` | 复制 Pod 进行调试 |

## 示例

### 示例 1: 使用 busybox 镜像调试 Pod

```bash
kubectl debug mypod -it --image=busybox
```

### 示例 2: 复制 Pod 并调试指定容器

```bash
kubectl debug mypod --copy-to=mydebugpod --container=main
```

### 示例 3: 调试节点

```bash
kubectl debug node/mynode -it --image=ubuntu
```

## 风险提示

> ⚠️ **MEDIUM**: 创建额外容器；注意资源消耗

## 所属维度

[[Kubernetes Troubleshooting-MOC|Kubernetes Troubleshooting]]
