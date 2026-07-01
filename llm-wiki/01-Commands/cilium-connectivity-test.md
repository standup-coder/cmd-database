---
{
  "cmd_name": "cilium connectivity test",
  "cmd_category": "Kubernetes Networking",
  "cmd_dimension": "Kubernetes Networking",
  "cmd_install": "Installed on nodes with Cilium CNI",
  "cmd_platforms": [
    "linux"
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

# cilium connectivity test

> Run connectivity test between pods

## 安装

```bash
Installed on nodes with Cilium CNI
```

## 用法

```
cilium connectivity test [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Namespace for test pods |

## 示例

### 示例 1: Run full connectivity test

```bash
cilium connectivity test
```

### 示例 2: Run test in specific namespace

```bash
cilium connectivity test --namespace test
```

## 风险提示

> ⚠️ **LOW**: Creates temporary test pods; cleaned up after test

## 所属维度

[[Kubernetes Networking-MOC|Kubernetes Networking]]
