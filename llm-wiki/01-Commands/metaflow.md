---
{
  "cmd_name": "metaflow",
  "cmd_category": "AI基础设施/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install metaflow",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "mlflow"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/more.yaml"
}
---

# metaflow

> Netflix 机器学习工作流框架

## 安装

```bash
pip install metaflow
```

## 用法

```
metaflow [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行 flow |
| `status` |  |
| `logs` |  |
| `card` |  |

## 示例

### 示例 1: 运行 Metaflow

```bash
python flow.py run
```

### 示例 2: 查看结果卡片

```bash
python flow.py card view
```

## 关联命令

- [[airflow]]
- [[mlflow]]

## 风险提示

> ⚠️ **MEDIUM**: Metaflow 会访问云存储和计算资源，请确认配置

## 所属维度

[[扩展命令-MOC|AI基础设施/扩展命令]]
