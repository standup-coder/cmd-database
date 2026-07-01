---
{
  "cmd_name": "hdfs",
  "cmd_category": "大数据/Hadoop生态",
  "cmd_dimension": "Hadoop生态",
  "cmd_install": "随 Hadoop 发行版安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hadoop",
    "yarn"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/hadoop.yaml"
}
---

# hdfs

> Hadoop 分布式文件系统（HDFS）管理命令

## 安装

```bash
随 Hadoop 发行版安装
```

## 用法

```
hdfs [OPTIONS] SUBCOMMAND [SUBCOMMAND OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-ls` | 列出目录内容 |
| `-rm -r` | 递归删除目录 |
| `-put` | 上传本地文件到 HDFS |

## 示例

### 示例 1: 上传本地文件到 HDFS

```bash
hdfs dfs -put local.txt /data/
```

### 示例 2: 查看 HDFS 集群状态报告

```bash
hdfs dfsadmin -report
```

## 关联命令

- [[hadoop]]
- [[yarn]]

## 风险提示

> ⚠️ **HIGH**: hdfs dfs -rm -r 为不可逆删除，建议在关键路径操作前备份

## 所属维度

[[Hadoop生态-MOC|大数据/Hadoop生态]]
