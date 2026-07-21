---
{
  "cmd_name": "oozie",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache Oozie 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "hue"
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

# oozie

> Apache Oozie 工作流调度

## 安装

```bash
随 Apache Oozie 安装
```

## 用法

```
oozie [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `job` | 作业管理 |
| `validate` | 验证 |
| `info` | 信息 |

## 示例

### 示例 1: 提交工作流

```bash
oozie job -oozie http://localhost:11000/oozie -config job.properties -run
```

### 示例 2: 验证 workflow

```bash
oozie validate workflow.xml
```

## 关联命令

- [[airflow]]

## 风险提示

> ⚠️ **MEDIUM**: Oozie 作业会调度 MapReduce/Hive 等，请确认依赖和资源

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
