---
{
  "cmd_name": "calicoctl delete networkpolicy",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Download from https://github.com/projectcalico/calico/releases",
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
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# calicoctl delete networkpolicy

> Delete Calico network policy

## 安装

```bash
Download from https://github.com/projectcalico/calico/releases
```

## 用法

```
calicoctl delete networkpolicy [policy-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Policy namespace |

## 示例

### 示例 1: Delete specific network policy

```bash
calicoctl delete networkpolicy allow-frontend -n production
```

### 示例 2: Delete policy defined in file

```bash
calicoctl delete -f policy.yaml
```

## 风险提示

> ⚠️ **HIGH**: Removing policy may expose services to unauthorized access

## 所属维度

[[Kubernetes Networking-MOC|Kubernetes Networking]]
