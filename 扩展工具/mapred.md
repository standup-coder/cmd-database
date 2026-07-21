---
{
  "cmd_name": "mapred",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 Hadoop 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hadoop",
    "yarn"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/extra.yaml"
}
---

# mapred

> Hadoop MapReduce 管理命令

## 安装

```bash
随 Hadoop 安装
```

## 用法

```
mapred [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `job` | 查看/管理作业 |
| `queues` | 查看队列 |
| `classpath` |  |

## 示例

### 示例 1: 列出所有 MapReduce 作业

```bash
mapred job -list
```

### 示例 2: 终止指定作业

```bash
mapred job -kill job_12345_0001
```

## 关联命令

- [[hadoop]]
- [[yarn]]

## 风险提示

> ⚠️ **MEDIUM**: 终止作业会影响计算结果，请确认后再执行

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
