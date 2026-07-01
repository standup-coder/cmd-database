---
{
  "cmd_name": "sql-client.sh",
  "cmd_category": "大数据/Flink流计算",
  "cmd_dimension": "Flink流计算",
  "cmd_install": "随 Apache Flink 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "flink"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/flink.yaml"
}
---

# sql-client.sh

> Flink SQL 交互式客户端

## 安装

```bash
随 Apache Flink 安装
```

## 用法

```
sql-client.sh [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 初始化 SQL 脚本 |
| `-f` | 执行 SQL 脚本文件 |

## 示例

### 示例 1: 启动 Flink SQL 客户端

```bash
sql-client.sh
```

### 示例 2: 执行 SQL 脚本文件

```bash
sql-client.sh -f queries.sql
```

## 关联命令

- [[flink]]

## 风险提示

> ⚠️ **MEDIUM**: DDL/DML 操作会修改表和作业，请在测试环境先验证

## 所属维度

[[Flink流计算-MOC|大数据/Flink流计算]]
