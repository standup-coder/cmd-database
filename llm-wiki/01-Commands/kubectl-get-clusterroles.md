---
{
  "cmd_name": "kubectl get clusterroles",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "kubectl built-in command",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# kubectl get clusterroles

> List ClusterRole resources for cluster-wide permissions

## 安装

```bash
kubectl built-in command
```

## 用法

```
kubectl get clusterroles [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format (wide, yaml, json) |

## 示例

### 示例 1: List all cluster roles

```bash
kubectl get clusterroles
```

### 示例 2: Get detailed YAML of all cluster roles

```bash
kubectl get clusterroles -o yaml
```

### 示例 3: Describe cluster-admin permissions

```bash
kubectl describe clusterrole cluster-admin
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; shows cluster permissions

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
