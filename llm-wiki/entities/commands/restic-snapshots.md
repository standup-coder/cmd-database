---
cmd_name: restic snapshots
cmd_category: "容器编排/K8s备份恢复"
cmd_dimension: Kubernetes Backup  Recovery
cmd_install: Download from https://restic.net/ or package manager
cmd_platforms:
- linux
- darwin
- windows
summary: "List restic backup snapshots"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-backup.yaml
---


# restic snapshots

> List restic backup snapshots

## 安装

```bash
Download from https://restic.net/ or package manager
```

## 用法

```
restic snapshots --repo [repository] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--repo` | Repository path |
| `--tag` | Filter by tag |

## 示例

### 示例 1: List all snapshots

```bash
restic snapshots --repo /backup/restic-repo
```

### 示例 2: List snapshots with specific tag

```bash
restic snapshots --repo s3:s3.amazonaws.com/bucket --tag production
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists snapshots only

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
