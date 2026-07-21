---
{
  "cmd_name": "hadoop",
  "cmd_category": "大数据/Hadoop生态",
  "cmd_dimension": "Hadoop生态",
  "cmd_install": "参考 https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hdfs",
    "yarn"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/hadoop.yaml"
}
---

# hadoop

> Hadoop 通用命令入口，可调用 fs、jar、dfsadmin 等子命令

## 安装

```bash
参考 https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
```

## 用法

```
hadoop [OPTIONS] SUBCOMMAND [SUBCOMMAND OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | 指定 Hadoop 配置目录 |
| `--loglevel` | 设置日志级别（DEBUG/INFO/WARN/ERROR） |

## 示例

### 示例 1: 列出 HDFS 根目录

```bash
hadoop fs -ls /
```

### 示例 2: 提交 MapReduce 作业

```bash
hadoop jar wordcount.jar WordCount /input /output
```

## 关联命令

- [[hdfs]]
- [[yarn]]

## 风险提示

> ⚠️ **HIGH**: 误删 HDFS 目录或覆盖输出路径会导致数据丢失，执行前请确认路径

## 所属维度

[[Hadoop生态-MOC|大数据/Hadoop生态]]
