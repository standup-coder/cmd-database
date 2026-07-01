---
{
  "cmd_name": "flux reconcile source git",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# flux reconcile source git

> Manually trigger Git source reconciliation

## 安装

```bash
Download from https://fluxcd.io/flux/installation/
```

## 用法

```
flux reconcile source git [source-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Source namespace |

## 示例

### 示例 1: Trigger reconciliation of flux-system source

```bash
flux reconcile source git flux-system
```

### 示例 2: Reconcile source in production namespace

```bash
flux reconcile source git myapp -n production
```

## 风险提示

> ⚠️ **MEDIUM**: Triggers immediate sync from Git; may deploy changes

## 所属维度

[[CD-MOC|Kubernetes CI/CD]]
