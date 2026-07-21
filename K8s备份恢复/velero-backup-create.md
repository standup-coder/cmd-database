---
{
  "cmd_name": "velero backup create",
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
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-backup.yaml"
}
---

# velero backup create

> Create backup of Kubernetes resources

## 安装

```bash
Download from https://velero.io/docs/main/basic-install/
```

## 用法

```
velero backup create [backup-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--include-namespaces` | Namespaces to include in backup |
| `--exclude-namespaces` | Namespaces to exclude from backup |
| `--include-resources` | Resource types to include |
| `--selector` | Label selector to filter resources |

## 示例

### 示例 1: Create full cluster backup

```bash
velero backup create mybackup
```

### 示例 2: Backup specific namespace

```bash
velero backup create prod-backup --include-namespaces production
```

### 示例 3: Backup only persistent volumes

```bash
velero backup create pv-backup --include-resources persistentvolumes,persistentvolumeclaims
```

### 示例 4: Backup resources with label selector

```bash
velero backup create app-backup --selector app=nginx
```

## 风险提示

> ⚠️ **LOW**: Read-only backup operation; no cluster modifications

## 所属维度

[[K8s备份恢复-MOC|Kubernetes Backup & Recovery]]
