---
{
  "cmd_name": "neptune",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install neptune",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wandb",
    "clearml"
  ],
  "cmd_tags": [
    "monitoring",
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# neptune

> Neptune ML实验管理平台，支持指标跟踪、模型版本、数据集版本管理

## 安装

```bash
pip install neptune
```

## 用法

```
neptune [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `sync` | 同步离线数据 |
| `status` | 查看同步状态 |

## 示例

### 示例 1: 初始化Neptune实验运行

```bash
python -c "import neptune; run = neptune.init_run(project='my-workspace/my-project')"
```

### 示例 2: 训练并记录到Neptune

```bash
python train.py --use_neptune --api_token $NEPTUNE_API_TOKEN
```

## 关联命令

- [[wandb]]
- [[clearml]]

## 风险提示

> ⚠️ **LOW**: 云端记录需注意数据隐私

## 参考链接

- [https://neptune.ai/](https://neptune.ai/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
