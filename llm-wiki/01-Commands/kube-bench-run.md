---
{
  "cmd_name": "kube-bench run",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "Download from https://github.com/aquasecurity/kube-bench/releases",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# kube-bench run

> Run CIS Kubernetes security benchmark checks

## 安装

```bash
Download from https://github.com/aquasecurity/kube-bench/releases
```

## 用法

```
kube-bench run [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--targets` | Target components: master, node, etcd, policies |
| `--json` | Output results in JSON format |
| `--config` | Configuration file path |

## 示例

### 示例 1: Run all security checks

```bash
kube-bench run
```

### 示例 2: Check control plane security only

```bash
kube-bench run --targets master
```

### 示例 3: Check worker node security only

```bash
kube-bench run --targets node
```

### 示例 4: Output results in JSON format

```bash
kube-bench run --json
```

## 风险提示

> ⚠️ **LOW**: Read-only assessment; checks configuration only

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
