---
{
  "cmd_name": "skaffold delete",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://skaffold.dev/docs/install/",
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
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# skaffold delete

> Delete Skaffold deployments

## 安装

```bash
Download from https://skaffold.dev/docs/install/
```

## 用法

```
skaffold delete [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Delete from specific namespace |

## 示例

### 示例 1: Delete deployed resources

```bash
skaffold delete
```

### 示例 2: Delete from dev namespace

```bash
skaffold delete --namespace dev
```

## 风险提示

> ⚠️ **HIGH**: Deletes application resources from cluster

## 所属维度

[[Kubernetes Development-MOC|Kubernetes Development]]
