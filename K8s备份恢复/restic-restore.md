---
{
  "cmd_name": "restic restore",
  "cmd_category": "Kubernetes Backup & Recovery",
  "cmd_dimension": "Kubernetes Backup  Recovery",
  "cmd_install": "Download from https://restic.net/ or package manager",
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
  "source_file": "data/container/k8s/k8s-backup.yaml"
}
---

# restic restore

> Restore from restic backup

## 安装

```bash
Download from https://restic.net/ or package manager
```

## 用法

```
restic restore [snapshot-id] --repo [repository] --target [path] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--repo` | Repository path |
| `--target` | Restore target path |

## 示例

### 示例 1: Restore latest snapshot

```bash
restic restore latest --repo /backup/restic-repo --target /restore
```

### 示例 2: Restore specific snapshot from S3

```bash
restic restore abc123 --repo s3:s3.amazonaws.com/bucket --target /restore
```

## 风险提示

> ⚠️ **HIGH**: Overwrites files in target directory

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
