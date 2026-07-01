---
{
  "cmd_name": "kubectl auth can-i",
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

# kubectl auth can-i

> Check if user has specific permissions

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl auth can-i [verb] [resource] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Check permissions in specific namespace |
| `--as` | Check permissions as specific user |
| `--as-group` | Check permissions as specific group |

## 示例

### 示例 1: Check if current user can get pods

```bash
kubectl auth can-i get pods
```

### 示例 2: Check if user has cluster-admin privileges

```bash
kubectl auth can-i '*' '*'
```

### 示例 3: Check deployment creation permission in production

```bash
kubectl auth can-i create deployments --namespace production
```

### 示例 4: Check service account permissions

```bash
kubectl auth can-i --as system:serviceaccount:default:my-sa get secrets
```

## 风险提示

> ⚠️ **LOW**: Read-only permission check; no operational changes

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
