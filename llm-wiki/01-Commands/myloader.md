---
{
  "cmd_name": "myloader",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 mydumper 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mydumper",
    "mysql"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# myloader

> 多线程恢复 mydumper 备份

## 安装

```bash
随 mydumper 安装
```

## 用法

```
myloader [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--directory` |  |
| `--threads` |  |
| `--database` |  |
| `--overwrite-tables` |  |

## 示例

### 示例 1: 恢复备份

```bash
myloader -u root -p password -d /backup -B mydb
```

### 示例 2: 4 线程恢复

```bash
myloader -d /backup --threads 4
```

## 关联命令

- [[mydumper]]
- [[mysql]]

## 风险提示

> ⚠️ **HIGH**: 恢复会覆盖目标库数据，请确认目标数据库正确

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
