---
cmd_name: helm uninstall
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Uninstall Helm release from cluster"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm uninstall

> Uninstall Helm release from cluster

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm uninstall [release-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Release namespace |
| `--keep-history` | Keep release history for rollback |
| `--no-hooks` | Skip pre-delete and post-delete hooks |

## 示例

### 示例 1: Uninstall nginx release

```bash
helm uninstall nginx
```

### 示例 2: Uninstall from production namespace

```bash
helm uninstall nginx -n production
```

### 示例 3: Uninstall but keep history

```bash
helm uninstall nginx --keep-history
```

### 示例 4: Uninstall without running hooks

```bash
helm uninstall nginx --no-hooks
```

## 风险提示

> ⚠️ **CRITICAL**: Removes all resources managed by release; causes service downtime

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
