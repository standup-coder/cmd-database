---
{
  "cmd_name": "beeline",
  "cmd_category": "大数据/查询引擎",
  "cmd_dimension": "查询引擎",
  "cmd_install": "随 Hive/HiveServer2 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hive",
    "presto"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/bigdata/query-engines.yaml"
}
---

# beeline

> HiveServer2 JDBC 客户端

## 安装

```bash
随 Hive/HiveServer2 安装
```

## 用法

```
beeline [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | JDBC URL |
| `-n` | 用户名 |
| `-p` | 密码 |

## 示例

### 示例 1: 连接 HiveServer2

```bash
beeline -u jdbc:hive2://localhost:10000 -n username -p password
```

### 示例 2: 执行 SQL 并退出

```bash
beeline -u jdbc:hive2://localhost:10000 -e "SHOW DATABASES"
```

## 关联命令

- [[hive]]
- [[presto]]

## 风险提示

> ⚠️ **LOW**: 命令行传入密码会留在历史记录中，建议使用配置文件或环境变量

## 所属维度

[[查询引擎-MOC|大数据/查询引擎]]
