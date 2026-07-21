---
{
  "cmd_name": "kubectl get limitrange",
  "cmd_category": "Kubernetes Troubleshooting",
  "cmd_dimension": "Kubernetes Troubleshooting",
  "cmd_install": "kubectl 内置命令",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-troubleshooting.yaml"
}
---

# kubectl get limitrange

> 检查资源限制范围

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl get limitrange [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |

## 示例

### 示例 1: 查看生产环境资源限制

```bash
kubectl get limits -n production
```

### 示例 2: 详细查看内存限制配置

```bash
kubectl describe limitrange mem-limit-range -n production
```

## 风险提示

> ⚠️ **LOW**: 只读限制信息；帮助识别资源约束问题

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
