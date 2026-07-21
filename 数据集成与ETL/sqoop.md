---
{
  "cmd_name": "sqoop",
  "cmd_category": "大数据/数据集成与ETL",
  "cmd_dimension": "数据集成与ETL",
  "cmd_install": "参考 https://sqoop.apache.org/",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hadoop",
    "hdfs"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/etl.yaml"
}
---

# sqoop

> Hadoop 与关系型数据库之间的数据传输工具

## 安装

```bash
参考 https://sqoop.apache.org/
```

## 用法

```
sqoop [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `import` | 从数据库导入到 HDFS |
| `export` | 从 HDFS 导出到数据库 |
| `--connect` | JDBC 连接字符串 |

## 示例

### 示例 1: 导入 MySQL 表到 HDFS

```bash
sqoop import --connect jdbc:mysql://localhost/db --table users --target-dir /data/users
```

### 示例 2: 导出 HDFS 目录到 MySQL 表

```bash
sqoop export --connect jdbc:mysql://localhost/db --table users --export-dir /data/users
```

## 关联命令

- [[hadoop]]
- [[hdfs]]

## 风险提示

> ⚠️ **HIGH**: 导入/导出涉及生产数据库，可能影响业务库性能，请避开高峰期

## 所属维度

[[数据集成与ETL-MOC|大数据/数据集成与ETL]]
