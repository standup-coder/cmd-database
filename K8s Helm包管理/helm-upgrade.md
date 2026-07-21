---
{
  "cmd_name": "helm upgrade",
  "cmd_category": "Kubernetes Helm Package Management",
  "cmd_dimension": "Kubernetes Helm Package Management",
  "cmd_install": "Download from https://helm.sh/docs/intro/install/",
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
  "source_file": "data/container/k8s/k8s-helm-enhanced.yaml"
}
---

# helm upgrade

> Upgrade Helm release to new version

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm upgrade [release-name] [chart] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Release namespace |
| `--install` | Install if release doesn't exist |
| `--values` | Values file path |
| `--set` | Set values on command line |
| `--atomic` | Rollback on failure |
| `--cleanup-on-fail` | Clean up new resources on upgrade failure |
| `--reset-values` | Reset values to chart defaults |
| `--reuse-values` | Reuse current values and merge with new ones |

## 示例

### 示例 1: Upgrade nginx release

```bash
helm upgrade nginx bitnami/nginx
```

### 示例 2: Upgrade or install if not exists

```bash
helm upgrade nginx bitnami/nginx --install
```

### 示例 3: Upgrade with new values

```bash
helm upgrade nginx bitnami/nginx --values new-values.yaml
```

### 示例 4: Upgrade with automatic rollback on failure

```bash
helm upgrade nginx bitnami/nginx --atomic
```

### 示例 5: Upgrade with specific image version

```bash
helm upgrade nginx bitnami/nginx --set image.tag=v2.0.0
```

## 风险提示

> ⚠️ **HIGH**: Modifies running applications; may cause service disruption

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
