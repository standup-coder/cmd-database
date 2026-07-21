---
{
  "cmd_name": "calicoctl get networkpolicies",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Download from https://github.com/projectcalico/calico/releases",
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

# calicoctl get networkpolicies

> List Calico network policies

## 安装

```bash
Download from https://github.com/projectcalico/calico/releases
```

## 用法

```
calicoctl get networkpolicies [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Filter by namespace |
| `-o` | Output format: yaml, json, wide |

## 示例

### 示例 1: List all network policies

```bash
calicoctl get networkpolicies
```

### 示例 2: List policies in production namespace

```bash
calicoctl get networkpolicies -n production
```

### 示例 3: Export policies in YAML format

```bash
calicoctl get networkpolicies -o yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists policies only

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
