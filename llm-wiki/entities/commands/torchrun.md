---
cmd_name: torchrun
cmd_category: AI基础设施/ML框架
cmd_dimension: ML框架
cmd_install: pip install torch
cmd_platforms:
- linux
- darwin
- windows
summary: "PyTorch分布式训练启动器"
cmd_level: advanced
cmd_related:
- tensorboard
cmd_tags:
- training
- distributed
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ml-frameworks.yaml
---


# torchrun

> PyTorch分布式训练启动器

## 安装

```bash
pip install torch
```

## 用法

```
torchrun [OPTIONS] SCRIPT.py [ARGS...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--nnodes` | 训练的节点数 |
| `--nproc_per_node` | 每个节点的进程数 (通常是GPU数量) |
| `--rdzv_id` | 唯一的作业ID |
| `--rdzv_backend` | 集合点后端 (例如 c10d) |
| `--rdzv_endpoint` | 集合点端点 (例如 master_addr:port) |

## 示例

### 示例 1: 在单机4卡上运行分布式训练

```bash
torchrun --nproc_per_node=4 train.py --batch_size=32
```

## 关联命令

- [[tensorboard]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 参考链接

- [https://pytorch.org/docs/stable/distributed.html#launch-utility](https://pytorch.org/docs/stable/distributed.html#launch-utility)

## 所属维度

[[ML框架-MOC|AI基础设施/ML框架]]
