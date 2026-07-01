---
{
  "cmd_name": "snowsql",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.snowflake.com/en/user-guide/snowsql-install-config",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "psql",
    "bigquery"
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

# snowsql

> Snowflake 数据仓库命令行客户端

## 安装

```bash
参考 https://docs.snowflake.com/en/user-guide/snowsql-install-config
```

## 用法

```
snowsql [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 账户 |
| `-u` | 用户 |
| `-d` | 数据库 |
| `-q` | 查询 |
| `-f` | 文件 |

## 示例

### 示例 1: 登录 Snowflake

```bash
snowsql -a myaccount -u myuser -d mydb
```

### 示例 2: 执行查询

```bash
snowsql -q 'SELECT CURRENT_VERSION()'
```

## 关联命令

- [[psql]]

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
