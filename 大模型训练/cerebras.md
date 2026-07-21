---
{
  "cmd_name": "cerebras",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "Cerebras软件栈",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "deepspeed",
    "megatron-lm"
  ],
  "cmd_tags": [
    "training",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# cerebras

> Cerebras Wafer-Scale Engine超大规模AI芯片训练平台，支持十亿到万亿参数模型

## 安装

```bash
Cerebras软件栈
```

## 用法

```
csrun_cpu [OPTIONS]
```

```
csrun_wse [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--cs-config` | Cerebras配置 |
| `--num_csx` | CS-2系统数量 |

## 示例

### 示例 1: 在Wafer-Scale Engine上运行训练

```bash
csrun_wse --cs-config config.yaml python train.py
```

### 示例 2: 查看 Cerebras 运行工具帮助

```bash
csrun_wse --help
```

## 关联命令

- [[deepspeed]]
- [[megatron-lm]]

## 风险提示

> ⚠️ **HIGH**: 专用硬件平台，成本极高

## 参考链接

- [https://www.cerebras.net/](https://www.cerebras.net/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
