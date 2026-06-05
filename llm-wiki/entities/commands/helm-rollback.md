---
cmd_name: helm rollback
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Rollback Helm release to previous version"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm rollback

> Rollback Helm release to previous version

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm rollback [release-name] [revision] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Release namespace |
| `--timeout` | Timeout for rollback |
| `--wait` | Wait for resources to be ready |

## 示例

### 示例 1: Rollback nginx to revision 1

```bash
helm rollback nginx 1
```

### 示例 2: Rollback to previous revision

```bash
helm rollback nginx 0
```

### 示例 3: View release history first

```bash
helm history nginx
```

### 示例 4: Rollback and wait for readiness

```bash
helm rollback nginx 2 --wait
```

## 风险提示

> ⚠️ **HIGH**: Reverts application to previous state; may cause service disruption

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
