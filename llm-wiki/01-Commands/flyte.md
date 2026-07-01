---
{
  "cmd_name": "flyte",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install flytekit",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "airflow",
    "kubeflow"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# flyte

> 大规模机器学习与数据工作流平台

## 安装

```bash
pip install flytekit
```

## 用法

```
flyte [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 本地运行 |
| `register` | 注册 |
| `pyflyte` |  |

## 示例

### 示例 1: 本地运行 workflow

```bash
pyflyte run workflow.py my_workflow
```

### 示例 2: 注册到 Flyte

```bash
pyflyte register workflow.py
```

## 关联命令

- [[airflow]]

## 风险提示

> ⚠️ **MEDIUM**: register 会部署到 Flyte 集群，请确认版本和依赖

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
