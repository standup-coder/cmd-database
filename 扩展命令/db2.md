---
{
  "cmd_name": "db2",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 IBM Db2 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sqlplus",
    "sqlcmd"
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

# db2

> IBM Db2 命令行处理器

## 安装

```bash
随 IBM Db2 安装
```

## 用法

```
db2 [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `connect` | to 连接 |
| `list` | tables |
| `terminate` |  |

## 示例

### 示例 1: 连接 sample 数据库

```bash
db2 connect to sample
```

### 示例 2: 执行 SQL

```bash
db2 'SELECT * FROM staff'
```

## 关联命令

- [[sqlplus]]
- [[sqlcmd]]

## 风险提示

> ⚠️ **MEDIUM**: Db2 命令可修改数据库对象，请在测试环境验证

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
