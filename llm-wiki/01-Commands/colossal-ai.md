---
{
  "cmd_name": "colossal-ai",
  "cmd_category": "AI基础设施/大模型训练",
  "cmd_dimension": "大模型训练",
  "cmd_install": "pip install colossalai",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "deepspeed",
    "accelerate"
  ],
  "cmd_tags": [
    "training",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-training.yaml"
}
---

# colossal-ai

> Colossal-AI统一深度学习加速系统，支持 Gemini、ZeRO、Pipeline 并行

## 安装

```bash
pip install colossalai
```

## 用法

```
colossalai run [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--nproc_per_node` | 每节点进程数 |
| `--host` | 主机文件 |
| `--master_addr` | 主节点地址 |

## 示例

### 示例 1: Colossal-AI启动8卡训练

```bash
colossalai run --nproc_per_node 8 train.py --config config.py
```

### 示例 2: 使用CLI启动器运行训练

```bash
python -m colossalai.cli.launch --nproc_per_node=4 train.py
```

## 关联命令

- [[deepspeed]]
- [[accelerate]]

## 风险提示

> ⚠️ **MEDIUM**: 并行策略选择不当影响训练效率

## 参考链接

- [https://colossalai.org/](https://colossalai.org/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
