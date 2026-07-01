---
{
  "cmd_name": "kfctl delete",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Download from https://github.com/kubeflow/kfctl/releases",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kfctl delete

> Delete Kubeflow deployment

## 安装

```bash
Download from https://github.com/kubeflow/kfctl/releases
```

## 用法

```
kfctl delete -f <config-file> [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Path to Kubeflow config file |
| `--delete_storage` | Delete storage resources |

## 示例

### 示例 1: Delete Kubeflow deployment

```bash
kfctl delete -f kfctl_k8s_istio.yaml
```

### 示例 2: Delete Kubeflow including storage

```bash
kfctl delete -f kfctl_aws.yaml --delete_storage
```

## 风险提示

> ⚠️ **CRITICAL**: Deletes entire Kubeflow installation

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
