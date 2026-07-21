---
{
  "cmd_name": "hbase shell",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Apache HBase 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "hive",
    "hdfs"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/extra.yaml"
}
---

# hbase shell

> HBase 交互式 Shell

## 安装

```bash
随 Apache HBase 安装
```

## 用法

```
hbase shell [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 非交互模式 |
| `-d` | 调试模式 |

## 示例

### 示例 1: 启动 HBase Shell

```bash
hbase shell
```

### 示例 2: 非交互列出表

```bash
echo 'list' | hbase shell -n
```

## 关联命令

- [[hive]]
- [[hdfs]]

## 风险提示

> ⚠️ **HIGH**: drop、disable 表会丢失数据，执行前请确认

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
