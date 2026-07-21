---
{
  "cmd_name": "pig",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache Hadoop/Pig 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hadoop",
    "hive"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# pig

> Apache Pig 大数据分析平台

## 安装

```bash
随 Apache Hadoop/Pig 安装
```

## 用法

```
pig [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-x` | local\|mapreduce |
| `-f` | 脚本 |
| `-param` | 参数 |

## 示例

### 示例 1: 以 MapReduce 模式运行

```bash
pig -x mapreduce script.pig
```

### 示例 2: 本地交互模式

```bash
pig -x local
```

## 关联命令

- [[hadoop]]
- [[hive]]

## 风险提示

> ⚠️ **MEDIUM**: Pig 脚本会读写 HDFS，请确认输入输出路径

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
