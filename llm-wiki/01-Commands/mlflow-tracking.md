---
{
  "cmd_name": "mlflow-tracking",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install mlflow",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wandb",
    "neptune"
  ],
  "cmd_tags": [
    "monitoring",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# mlflow-tracking

> MLflow Tracking模块，本地实验跟踪与模型注册

## 安装

```bash
pip install mlflow
```

## 用法

```
mlflow ui [OPTIONS]
```

```
python train.py (使用mlflow库)
```

## 参数

| Flag | Description |
|------|-------------|
| `ui` | 启动跟踪UI |
| `--backend-store-uri` | 后端存储URI |
| `--default-artifact-root` | 制品默认存储路径 |

## 示例

### 示例 1: 本地启动MLflow UI

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000
```

### 示例 2: 生产级MLflow跟踪服务器

```bash
mlflow server --backend-store-uri postgresql://mlflow@localhost/mlflow --default-artifact-root s3://mlflow-artifacts
```

## 关联命令

- [[wandb]]
- [[neptune]]

## 风险提示

> ⚠️ **LOW**: 本地部署数据安全

## 参考链接

- [https://mlflow.org/docs/latest/tracking.html](https://mlflow.org/docs/latest/tracking.html)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
