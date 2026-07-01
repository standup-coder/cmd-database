---
{
  "cmd_name": "mydumper",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://github.com/mydumper/mydumper/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "myloader",
    "mysqldump"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# mydumper

> 多线程 MySQL 逻辑备份工具

## 安装

```bash
参考 https://github.com/mydumper/mydumper/releases
```

## 用法

```
mydumper [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--outputdir` |  |
| `--threads` |  |
| `--rows` |  |
| `--regex` |  |

## 示例

### 示例 1: 备份数据库

```bash
mydumper -u root -p password -B mydb -o /backup
```

### 示例 2: 4 线程备份

```bash
mydumper -B mydb --threads 4 -o /backup
```

## 关联命令

- [[myloader]]
- [[mysqldump]]

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
