---
{
  "cmd_name": "velero backup list",
  "cmd_category": "Kubernetes Backup & Recovery",
  "cmd_dimension": "Kubernetes Backup  Recovery",
  "cmd_install": "Download from https://velero.io/docs/main/basic-install/",
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

# velero backup list

> List all Velero backups

## 安装

```bash
Download from https://velero.io/docs/main/basic-install/
```

## 用法

```
velero backup list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | Output format: table, json, yaml |

## 示例

### 示例 1: List all backups

```bash
velero backup list
```

### 示例 2: List backups in JSON format

```bash
velero backup list -o json
```

### 示例 3: Show detailed backup information

```bash
velero backup describe mybackup
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists backups only

## 所属维度

[[Kubernetes Backup  Recovery-MOC|Kubernetes Backup & Recovery]]
