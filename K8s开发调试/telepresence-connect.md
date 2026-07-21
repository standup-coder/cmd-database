---
{
  "cmd_name": "telepresence connect",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://www.telepresence.io/docs/latest/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# telepresence connect

> Connect local environment to Kubernetes cluster

## 安装

```bash
Download from https://www.telepresence.io/docs/latest/install/
```

## 用法

```
telepresence connect [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Connect to specific namespace |
| `--context` | Kubernetes context |

## 示例

### 示例 1: Connect to cluster

```bash
telepresence connect
```

### 示例 2: Connect to production namespace

```bash
telepresence connect --namespace production
```

### 示例 3: Check connection status

```bash
telepresence status
```

## 风险提示

> ⚠️ **MEDIUM**: Creates network proxy to cluster

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
