---
{
  "cmd_name": "helm lint",
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

# helm lint

> Lint chart for best practices and errors

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm lint [chart-path] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--values` | Values file for linting |
| `--set` | Set values for linting |
| `--strict` | Fail on lint warnings |

## 示例

### 示例 1: Lint chart in mychart directory

```bash
helm lint mychart
```

### 示例 2: Lint with custom values

```bash
helm lint mychart --values values.yaml
```

### 示例 3: Strict linting mode

```bash
helm lint mychart --strict
```

## 风险提示

> ⚠️ **LOW**: Static analysis only; validates chart structure

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
