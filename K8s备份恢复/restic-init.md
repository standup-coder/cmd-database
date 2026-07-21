---
{
  "cmd_name": "restic init",
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

# restic init

> Initialize restic backup repository

## 安装

```bash
Download from https://restic.net/ or package manager
```

## 用法

```
restic init --repo [repository-path]
```

## 示例

### 示例 1: Initialize local backup repository

```bash
restic init --repo /backup/restic-repo
```

### 示例 2: Initialize S3 backup repository

```bash
restic init --repo s3:s3.amazonaws.com/my-backup-bucket
```

## 风险提示

> ⚠️ **LOW**: Creates empty repository; no data operations

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
