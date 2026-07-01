---
{
  "cmd_name": "ysqlsh",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 YugabyteDB 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "psql",
    "ycqlsh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# ysqlsh

> YugabyteDB 兼容 PostgreSQL 的 SQL Shell

## 安装

```bash
随 YugabyteDB 安装
```

## 用法

```
ysqlsh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | 主机 |
| `-p` | 端口 |
| `-d` | 数据库 |
| `-c` | 执行命令 |

## 示例

### 示例 1: 连接本地 YugabyteDB

```bash
ysqlsh -h localhost -d yugabyte
```

### 示例 2: 执行 SQL

```bash
ysqlsh -c 'SELECT version();'
```

## 关联命令

- [[psql]]
- [[ycqlsh]]

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
