---
{
  "cmd_name": "sqlplus",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Oracle 客户端或 Instant Client 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mysql",
    "psql"
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

# sqlplus

> Oracle 数据库 SQL*Plus 客户端

## 安装

```bash
随 Oracle 客户端或 Instant Client 安装
```

## 用法

```
sqlplus [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 静默模式 |
| `-l` | 只登录 |
| `/@TNS` | 连接串 |

## 示例

### 示例 1: 连接 Oracle

```bash
sqlplus username/password@database
```

### 示例 2: 以 sysdba 执行 SQL

```bash
sqlplus -s / as sysdba <<EOF
SELECT * FROM dual;
EOF
```

## 关联命令

- [[mysql]]
- [[psql]]

## 风险提示

> ⚠️ **HIGH**: 以 SYSDBA 连接可操作整个数据库，请严格控制权限

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
