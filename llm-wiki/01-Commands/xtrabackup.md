---
{
  "cmd_name": "xtrabackup",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.percona.com/percona-xtrabackup",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mysql",
    "mysqldump"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# xtrabackup

> Percona XtraBackup 热备份工具

## 安装

```bash
参考 https://docs.percona.com/percona-xtrabackup
```

## 用法

```
xtrabackup [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--backup` |  |
| `--prepare` |  |
| `--target-dir` |  |
| `--user` |  |
| `--password` |  |

## 示例

### 示例 1: 全量热备份

```bash
xtrabackup --backup --target-dir=/backup/full
```

### 示例 2: 准备备份

```bash
xtrabackup --prepare --target-dir=/backup/full
```

## 关联命令

- [[mysql]]
- [[mysqldump]]

## 风险提示

> ⚠️ **MEDIUM**: prepare 会修改备份文件，请保留原始备份副本

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
