---
{
  "cmd_name": "kubectl get events",
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

# kubectl get events

> 获取集群事件信息，用于故障诊断

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl get events [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |
| `-A` | 所有命名空间 |
| `--sort-by` | 按字段排序 |
| `--field-selector` | 字段选择器过滤 |

## 示例

### 示例 1: 查看生产环境事件

```bash
kubectl get events -n production
```

### 示例 2: 按时间排序查看所有事件

```bash
kubectl get events -A --sort-by='.lastTimestamp'
```

### 示例 3: 只查看警告类型事件

```bash
kubectl get events --field-selector type=Warning
```

## 风险提示

> ⚠️ **LOW**: 只读操作；显示事件日志

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
