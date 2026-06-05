---
cmd_name: velero schedule create
cmd_category: "容器编排/K8s备份恢复"
cmd_dimension: Kubernetes Backup  Recovery
cmd_install: Download from https://velero.io/docs/main/basic-install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Create scheduled backup"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-backup.yaml
---


# velero schedule create

> Create scheduled backup

## 安装

```bash
Download from https://velero.io/docs/main/basic-install/
```

## 用法

```
velero schedule create [schedule-name] --schedule [cron-expression] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--schedule` | Cron expression for schedule |
| `--include-namespaces` | Namespaces to include |

## 示例

### 示例 1: Schedule daily backup at 2 AM

```bash
velero schedule create daily-backup --schedule '0 2 * * *'
```

### 示例 2: Schedule hourly backup for production namespace

```bash
velero schedule create hourly-backup --schedule '@hourly' --include-namespaces production
```

## 风险提示

> ⚠️ **LOW**: Creates scheduled task; actual backups are read-only

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
