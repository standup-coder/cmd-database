---
{
  "cmd_name": "trivy config",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "Download from https://aquasecurity.github.io/trivy/",
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
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# trivy config

> Scan configuration files for misconfigurations

## 安装

```bash
Download from https://aquasecurity.github.io/trivy/
```

## 用法

```
trivy config [path] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--format` | Output format: table, json |

## 示例

### 示例 1: Scan Kubernetes manifest

```bash
trivy config deployment.yaml
```

### 示例 2: Scan directory of manifests

```bash
trivy config manifests/
```

### 示例 3: Scan Helm chart with JSON output

```bash
trivy config --format json helm-chart/
```

## 风险提示

> ⚠️ **LOW**: Read-only scanning; no file modifications

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
