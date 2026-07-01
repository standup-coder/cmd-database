---
{
  "cmd_name": "kubectl get",
  "cmd_category": "Container Orchestration",
  "cmd_dimension": "Container Orchestration",
  "cmd_install": "Download from https://kubernetes.io/docs/tasks/tools/",
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
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl get

> Display one or many resources

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl get [resource] [name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: json\|yaml\|wide\|name\|custom-columns |
| `-n` | Namespace to query |
| `-A` | List resources across all namespaces |
| `-w` | Watch for changes |
| `--show-labels` | Show all labels |

## 示例

### 示例 1: List all pods in default namespace

```bash
kubectl get pods
```

### 示例 2: List pods in production namespace

```bash
kubectl get pods -n production
```

### 示例 3: List all pods in all namespaces

```bash
kubectl get pods -A
```

### 示例 4: Get pods in YAML format

```bash
kubectl get pods -o yaml
```

### 示例 5: List all cluster nodes

```bash
kubectl get nodes
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Container Orchestration-MOC|Container Orchestration]]
