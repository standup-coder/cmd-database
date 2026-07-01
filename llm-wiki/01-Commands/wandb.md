---
{
  "cmd_name": "wandb",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install wandb",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "neptune",
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

# wandb

> Weights & Biases实验跟踪平台，记录指标、超参数、模型版本、数据集血缘

## 安装

```bash
pip install wandb
```

## 用法

```
wandb [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `login` | 登录W&B账号 |
| `init` | 初始化项目 |
| `sync` | 同步离线实验数据 |
| `artifact` | 管理模型和数据集制品 |

## 示例

### 示例 1: 登录Weights & Biases

```bash
wandb login
```

### 示例 2: 训练并自动记录到W&B

```bash
python train.py --use_wandb --project my-project --name experiment-1
```

### 示例 3: 上传模型制品

```bash
wandb artifact put model.pt --name my-model --type model
```

## 关联命令

- [[neptune]]
- [[clearml]]

## 风险提示

> ⚠️ **LOW**: 云端记录需注意数据隐私

## 参考链接

- [https://wandb.ai/](https://wandb.ai/)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
