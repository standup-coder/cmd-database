---
{
  "cmd_name": "restic backup",
  "cmd_category": "Kubernetes Backup & Recovery",
  "cmd_dimension": "Kubernetes Backup  Recovery",
  "cmd_install": "Download from https://restic.net/ or package manager",
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
  "source_file": "data/container/k8s/k8s-backup.yaml"
}
---

# restic backup

> Create restic backup

## 安装

```bash
Download from https://restic.net/ or package manager
```

## 用法

```
restic backup [path] --repo [repository] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--repo` | Repository path |
| `--exclude` | Exclude pattern |
| `--tag` | Tags for backup |

## 示例

### 示例 1: Backup directory to repository

```bash
restic backup /data --repo /backup/restic-repo
```

### 示例 2: Backup to S3 with tag

```bash
restic backup /data --repo s3:s3.amazonaws.com/bucket --tag production
```

### 示例 3: Backup etcd data directory

```bash
restic backup /var/lib/etcd --repo /backup/etcd-backup
```

## 风险提示

> ⚠️ **LOW**: Read-only backup operation; no data modification

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
