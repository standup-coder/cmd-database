---
{
  "cmd_name": "flink",
  "cmd_category": "大数据/Flink流计算",
  "cmd_dimension": "Flink流计算",
  "cmd_install": "参考 https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/local_installation/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sql-client.sh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/flink.yaml"
}
---

# flink

> Flink 作业提交与管理 CLI

## 安装

```bash
参考 https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/local_installation/
```

## 用法

```
flink [OPTIONS] [ACTION]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 提交 Flink 作业 |
| `list` | 列出运行中的作业 |
| `cancel` | 取消指定作业 |

## 示例

### 示例 1: 提交 Flink 作业

```bash
flink run -c org.example.Job myjob.jar
```

### 示例 2: 列出运行中的 Flink 作业

```bash
flink list
```

## 关联命令

- [[sql-clientsh]]

## 风险提示

> ⚠️ **MEDIUM**: 取消作业会中断数据流，请先确认Checkpoint状态

## 所属维度

[[Flink流计算-MOC|大数据/Flink流计算]]
