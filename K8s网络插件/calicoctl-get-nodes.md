---
{
  "cmd_name": "calicoctl get nodes",
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

# calicoctl get nodes

> List all Calico nodes

## 安装

```bash
Download from https://github.com/projectcalico/calico/releases
```

## 用法

```
calicoctl get nodes [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: yaml, json, wide |

## 示例

### 示例 1: List all Calico nodes

```bash
calicoctl get nodes
```

### 示例 2: List nodes with detailed information

```bash
calicoctl get nodes -o wide
```

### 示例 3: List nodes in YAML format

```bash
calicoctl get nodes -o yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists nodes only

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
