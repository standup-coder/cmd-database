---
cmd_name: deepspeed
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install deepspeed
cmd_platforms:
- linux
- darwin
- windows
summary: "微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload"
cmd_level: advanced
cmd_related:
- accelerate
- torchrun
cmd_tags:
- training
- distributed
- advanced
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# deepspeed

> 微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload

## 安装

```bash
pip install deepspeed
```

## 用法

```
deepspeed [OPTIONS] SCRIPT.py [ARGS...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--num_gpus` | 使用的GPU数量 |
| `--master_port` | 分布式训练主节点端口 |
| `--include` | 指定使用的GPU，如 'localhost:0,1,2,3' |
| `--exclude` | 排除指定的GPU |

## 示例

### 示例 1: 使用4张GPU和DeepSpeed配置文件启动训练

```bash
deepspeed --num_gpus=4 train.py --deepspeed ds_config.json
```

### 示例 2: 指定使用8张GPU进行训练

```bash
deepspeed --include='localhost:0,1,2,3,4,5,6,7' train.py
```

### 示例 3: 使用ZeRO-3优化策略训练大模型

```bash
deepspeed train.py --deepspeed ds_config_zero3.json
```

## 关联命令

- [[accelerate]]
- [[torchrun]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模分布式训练消耗大量GPU资源，需合理配置

## 参考链接

- [https://www.deepspeed.ai/](https://www.deepspeed.ai/)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
