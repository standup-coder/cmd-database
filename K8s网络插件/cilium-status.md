---
{
  "cmd_name": "cilium status",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Installed on nodes with Cilium CNI",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-network.yaml"
}
---

# cilium status

> Check Cilium agent status

## 安装

```bash
Installed on nodes with Cilium CNI
```

## 用法

```
cilium status [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--wait` | Wait for Cilium to be ready |
| `-o` | Output format: json, jsonpath, yaml |

## 示例

### 示例 1: Display Cilium agent status

```bash
cilium status
```

### 示例 2: Wait for Cilium to become ready

```bash
cilium status --wait
```

### 示例 3: Display status in JSON format

```bash
cilium status -o json
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no operational impact

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
