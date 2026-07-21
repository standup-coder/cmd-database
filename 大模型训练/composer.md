---
{
  "cmd_name": "composer",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install mosaicml",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lightning",
    "deepspeed"
  ],
  "cmd_tags": [
    "training",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# composer

> MosaicML Composer高效训练库，内置100+算法和优化方法

## 安装

```bash
pip install mosaicml
```

## 用法

```
composer [OPTIONS] SCRIPT.py
```

## 参数

| Flag | Description |
|------|-------------|
| `--fsdp_config` | FSDP配置文件 |
| `--autoresume` | 自动从断点恢复 |
| `--run_name` | 实验名称 |

## 示例

### 示例 1: FSDP训练

```bash
composer train.py --fsdp_config fsdp_config.yaml
```

### 示例 2: 启用多个训练优化算法

```bash
composer train.py --algorithms BlurPool SAM LabelSmoothing
```

## 关联命令

- [[lightning]]
- [[deepspeed]]

## 风险提示

> ⚠️ **LOW**: 算法组合需验证兼容性

## 参考链接

- [https://www.mosaicml.com/](https://www.mosaicml.com/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
