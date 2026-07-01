---
{
  "cmd_name": "kubectl get resourcequotas",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "kubectl built-in command",
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
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# kubectl get resourcequotas

> List ResourceQuota resources for namespace quotas

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get resourcequotas [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |

## 示例

### 示例 1: List quotas in production namespace

```bash
kubectl get quota -n production
```

### 示例 2: Describe compute resource quota

```bash
kubectl describe resourcequota compute-resources -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows resource allocations

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
