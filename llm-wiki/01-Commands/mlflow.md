---
{
  "cmd_name": "mlflow",
  "cmd_category": "AI基础设施/MLOps平台",
  "cmd_dimension": "MLOps平台",
  "cmd_install": "pip install mlflow",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kfp"
  ],
  "cmd_tags": [
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/mlops.yaml"
}
---

# mlflow

> MLflow 命令行客户端，用于模型全生命周期管理

## 安装

```bash
pip install mlflow
```

## 用法

```
mlflow [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行一个MLflow项目 |
| `ui` | 启动MLflow跟踪UI |
| `models` | 管理模型 (serve, predict, build-docker) |
| `artifacts` | 下载或上传产物 |

## 示例

### 示例 1: 启动UI，使用SQLite作为后端存储

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

### 示例 2: 运行当前项目的'train'入口点，并传递参数

```bash
mlflow run . -e train --P alpha=0.5
```

### 示例 3: 将指定运行产出的模型部署为一个本地服务

```bash
mlflow models serve -m runs:/<run_id>/model -p 1234
```

## 关联命令

- [[kfp]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 参考链接

- [https://mlflow.org/docs/latest/cli.html](https://mlflow.org/docs/latest/cli.html)

## 所属维度

[[MLOps平台-MOC|AI基础设施/MLOps平台]]
