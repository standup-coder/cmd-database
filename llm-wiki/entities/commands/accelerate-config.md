---
cmd_name: accelerate-config
cmd_category: AI基础设施/模型架构
cmd_dimension: 模型架构
cmd_install: pip install accelerate
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Accelerate配置向导，交互式生成分布式训练配置文件"
cmd_level: advanced
cmd_related:
- accelerate
- deepspeed
cmd_tags:
- training
- architecture
- distributed
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/model-architecture.yaml
---


# accelerate-config

> HuggingFace Accelerate配置向导，交互式生成分布式训练配置文件

## 安装

```bash
pip install accelerate
```

## 用法

```
accelerate config [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config_file` | 配置文件输出路径 |
| `--machine_rank` | 机器rank |
| `--num_machines` | 机器数量 |
| `--num_processes` | 进程数量 |

## 示例

### 示例 1: 交互式生成配置文件

```bash
accelerate config
```

### 示例 2: 指定输出路径

```bash
accelerate config --config_file default_config.yaml
```

### 示例 3: 使用配置文件启动训练

```bash
accelerate launch --config_file config.yaml train.py
```

## 关联命令

- [[accelerate]]
- [[deepspeed]]

## 风险提示

> ⚠️ **LOW**: 配置工具安全

## 参考链接

- [https://huggingface.co/docs/accelerate](https://huggingface.co/docs/accelerate)

## 所属维度

[[模型架构-MOC|AI基础设施/模型架构]]
