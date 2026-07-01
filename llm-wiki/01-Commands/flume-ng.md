---
{
  "cmd_name": "flume-ng",
  "cmd_category": "大数据/数据集成与ETL",
  "cmd_dimension": "数据集成与ETL",
  "cmd_install": "参考 https://flume.apache.org/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kafka-console-producer",
    "airflow"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/etl.yaml"
}
---

# flume-ng

> Apache Flume 分布式日志采集命令

## 安装

```bash
参考 https://flume.apache.org/
```

## 用法

```
flume-ng agent [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | Agent 名称 |
| `--conf` | 配置目录 |
| `--conf-file` | 配置文件路径 |

## 示例

### 示例 1: 启动 Flume Agent

```bash
flume-ng agent --name a1 --conf conf --conf-file conf/flume.conf
```

### 示例 2: 查看 Flume 版本

```bash
flume-ng version
```

## 关联命令

- [[kafka-console-producer]]
- [[airflow]]

## 风险提示

> ⚠️ **MEDIUM**: 配置错误可能导致数据丢失或重复，请检查 channel 容量与 sink 可靠性

## 所属维度

[[数据集成与ETL-MOC|大数据/数据集成与ETL]]
