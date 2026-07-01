---
{
  "cmd_name": "hive",
  "cmd_category": "大数据/查询引擎",
  "cmd_dimension": "查询引擎",
  "cmd_install": "参考 https://hive.apache.org/downloads.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "beeline",
    "presto"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/query-engines.yaml"
}
---

# hive

> Apache Hive 命令行接口

## 安装

```bash
参考 https://hive.apache.org/downloads.html
```

## 用法

```
hive [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 执行 SQL 语句 |
| `-f` | 执行 SQL 文件 |
| `--database` | 指定默认数据库 |

## 示例

### 示例 1: 执行 Hive SQL 查询

```bash
hive -e "SELECT * FROM users LIMIT 10"
```

### 示例 2: 执行 HQL 脚本文件

```bash
hive -f query.hql --database mydb
```

## 关联命令

- [[beeline]]
- [[presto]]

## 风险提示

> ⚠️ **MEDIUM**: 全表扫描可能产生大 job，请确认分区过滤和 LIMIT

## 所属维度

[[查询引擎-MOC|大数据/查询引擎]]
