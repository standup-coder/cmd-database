---
{
  "cmd_name": "kubectl logs -l serving.kserve.io/inferenceservice",
  "cmd_category": "Kubernetes MLOps",
  "cmd_dimension": "Kubernetes MLOps",
  "cmd_install": "Requires KServe deployment",
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
  "source_file": "data/container/k8s/k8s-mlops.yaml"
}
---

# kubectl logs -l serving.kserve.io/inferenceservice

> View logs for KServe model serving pods

## 安装

```bash
Requires KServe deployment
```

## 用法

```
kubectl logs -l serving.kserve.io/inferenceservice=<name> [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Container name (kserve-container, queue-proxy) |
| `-f` | Follow log output |
| `--tail` | Lines of recent log to display |

## 示例

### 示例 1: View model container logs

```bash
kubectl logs -l serving.kserve.io/inferenceservice=sklearn-iris -c kserve-container
```

### 示例 2: Follow logs for inference service

```bash
kubectl logs -l serving.kserve.io/inferenceservice=my-model -f
```

## 风险提示

> ⚠️ **LOW**: Read-only operation

## 所属维度

[[Kubernetes MLOps-MOC|Kubernetes MLOps]]
