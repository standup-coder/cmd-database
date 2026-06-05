---
cmd_name: velero restore create
cmd_category: "容器编排/K8s备份恢复"
cmd_dimension: Kubernetes Backup  Recovery
cmd_install: Download from https://velero.io/docs/main/basic-install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Restore from Velero backup"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/container/k8s-backup.yaml
---


# velero restore create

> Restore from Velero backup

## 安装

```bash
Download from https://velero.io/docs/main/basic-install/
```

## 用法

```
velero restore create [restore-name] --from-backup [backup-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--from-backup` | Backup name to restore from |
| `--include-namespaces` | Namespaces to restore |
| `--namespace-mappings` | Map namespaces during restore |

## 示例

### 示例 1: Restore from backup

```bash
velero restore create --from-backup mybackup
```

### 示例 2: Restore specific namespace

```bash
velero restore create prod-restore --from-backup prod-backup --include-namespaces production
```

### 示例 3: Restore with namespace mapping

```bash
velero restore create --from-backup mybackup --namespace-mappings old-ns:new-ns
```

## 风险提示

> ⚠️ **CRITICAL**: Restores resources to cluster; may overwrite existing resources

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
