---
{
  "cmd_name": "helm package",
  "cmd_category": "Kubernetes Helm Package Management",
  "cmd_dimension": "Kubernetes Helm Package Management",
  "cmd_install": "Download from https://helm.sh/docs/intro/install/",
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
  "source_file": "data/container/k8s/k8s-helm-enhanced.yaml"
}
---

# helm package

> Package chart into versioned archive

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm package [chart-path] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--version` | Override chart version |
| `--app-version` | Override app version |
| `--destination` | Location to write the chart package |

## 示例

### 示例 1: Package chart in mychart directory

```bash
helm package mychart
```

### 示例 2: Package with specific version

```bash
helm package mychart --version 1.2.3
```

### 示例 3: Package to specific directory

```bash
helm package mychart --destination /tmp/packages
```

## 风险提示

> ⚠️ **LOW**: Creates chart archive; no cluster impact

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
