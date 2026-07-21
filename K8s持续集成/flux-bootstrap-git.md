---
{
  "cmd_name": "flux bootstrap git",
  "cmd_category": "Kubernetes CI/CD",
  "cmd_dimension": "CD",
  "cmd_install": "Download from https://fluxcd.io/flux/installation/",
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
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# flux bootstrap git

> Bootstrap Flux to Git repository

## 安装

```bash
Download from https://fluxcd.io/flux/installation/
```

## 用法

```
flux bootstrap git [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--url` | Git repository URL |
| `--branch` | Git branch |
| `--path` | Path in repository for Flux manifests |
| `--token-auth` | Use token authentication |

## 示例

### 示例 1: Bootstrap Flux to Git repository

```bash
flux bootstrap git --url=https://github.com/example/repo --branch=main --path=clusters/production
```

### 示例 2: Bootstrap to GitHub with personal access token

```bash
flux bootstrap github --owner=myorg --repository=fleet --path=clusters/production --personal
```

## 风险提示

> ⚠️ **HIGH**: Installs Flux components to cluster; modifies Git repository

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
