---
{
  "cmd_name": "flux get kustomizations",
  "cmd_category": "Kubernetes CI/CD",
  "cmd_dimension": "CD",
  "cmd_install": "Download from https://fluxcd.io/flux/installation/",
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
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# flux get kustomizations

> List Flux Kustomization resources

## 安装

```bash
Download from https://fluxcd.io/flux/installation/
```

## 用法

```
flux get kustomizations [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-A` | All namespaces |
| `--watch` | Watch for changes |

## 示例

### 示例 1: List kustomizations in current namespace

```bash
flux get kustomizations
```

### 示例 2: List kustomizations in all namespaces

```bash
flux get kustomizations -A
```

### 示例 3: Watch kustomization changes in real-time

```bash
flux get kustomizations --watch
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists resources only

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
