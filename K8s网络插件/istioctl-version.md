---
{
  "cmd_name": "istioctl version",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Download from https://istio.io/latest/docs/setup/getting-started/#download",
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
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# istioctl version

> Check Istio service mesh version

## 安装

```bash
Download from https://istio.io/latest/docs/setup/getting-started/#download
```

## 用法

```
istioctl version [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--remote` | Check remote cluster version |
| `--short` | Show short version output |

## 示例

### 示例 1: Display Istio client and control plane versions

```bash
istioctl version
```

### 示例 2: Check version of Istio control plane

```bash
istioctl version --remote
```

### 示例 3: Show concise version information

```bash
istioctl version --short
```

## 风险提示

> ⚠️ **LOW**: Read-only version check

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
