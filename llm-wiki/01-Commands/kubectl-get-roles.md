---
{
  "cmd_name": "kubectl get roles",
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

# kubectl get roles

> List Role resources for namespace-scoped permissions

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get roles [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Specify namespace |
| `-A` | All namespaces |
| `-o` | Output format (wide, yaml, json) |

## 示例

### 示例 1: List roles in production namespace

```bash
kubectl get roles -n production
```

### 示例 2: List all roles with detailed permissions

```bash
kubectl get roles -A -o wide
```

### 示例 3: Describe specific role configuration

```bash
kubectl describe role admin-role -n production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows permission mappings

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
