---
{
  "cmd_name": "kubectl api-resources",
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

# kubectl api-resources

> 列出所有可用的 API 资源

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl api-resources [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespaced` | 只显示命名空间作用域资源 |
| `--verbs` | 按支持的操作过滤 |

## 示例

### 示例 1: 列出所有 API 资源

```bash
kubectl api-resources
```

### 示例 2: 只显示命名空间内资源

```bash
kubectl api-resources --namespaced=true
```

### 示例 3: 显示支持 list/get 操作的资源

```bash
kubectl api-resources --verbs=list,get
```

## 风险提示

> ⚠️ **LOW**: 只读 API 信息；帮助理解集群能力

## 所属维度

[[Kubernetes Troubleshooting-MOC|Kubernetes Troubleshooting]]
