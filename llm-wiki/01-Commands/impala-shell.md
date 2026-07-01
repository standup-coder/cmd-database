---
{
  "cmd_name": "impala-shell",
  "cmd_category": "大数据/查询引擎",
  "cmd_dimension": "查询引擎",
  "cmd_install": "随 Apache Impala 或 CDH 安装",
  "cmd_platforms": [
    "linux"
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/query-engines.yaml"
}
---

# impala-shell

> Impala 交互式 SQL Shell

## 安装

```bash
随 Apache Impala 或 CDH 安装
```

## 用法

```
impala-shell [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 指定 Impala daemon 地址 |
| `-q` | 执行 SQL 查询 |

## 示例

### 示例 1: 连接本地 Impala daemon

```bash
impala-shell -i localhost:21000
```

### 示例 2: 执行查询并退出

```bash
impala-shell -i localhost:21000 -q "SELECT * FROM users LIMIT 10"
```

## 关联命令

- [[hive]]
- [[presto]]

## 风险提示

> ⚠️ **MEDIUM**: Impala 适合交互式查询，避免执行超大表的全表扫描

## 所属维度

[[查询引擎-MOC|大数据/查询引擎]]
