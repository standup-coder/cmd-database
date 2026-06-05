---
cmd_name: weights-biases-sweep
cmd_category: AI基础设施/监控与评估
cmd_dimension: 监控与评估
cmd_install: pip install wandb
cmd_platforms:
- linux
- darwin
- windows
summary: "W&B超参数搜索(Sweep)，支持网格搜索、随机搜索、贝叶斯优化"
cmd_level: intermediate
cmd_related:
- wandb
- optimum-cli
cmd_tags:
- monitoring
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/monitoring.yaml
---


# weights-biases-sweep

> W&B超参数搜索(Sweep)，支持网格搜索、随机搜索、贝叶斯优化

## 安装

```bash
pip install wandb
```

## 用法

```
wandb sweep [OPTIONS]
```

```
wandb agent [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `sweep` | 创建超参数搜索配置 |
| `agent` | 启动搜索代理 |
| `--project` | W&B项目名称 |

## 示例

### 示例 1: 创建sweep并获取sweep ID

```bash
wandb sweep sweep_config.yaml
```

### 示例 2: 启动代理执行超参数搜索

```bash
wandb agent my-workspace/my-project/sweep_id
```

## 关联命令

- [[wandb]]
- [[optimum-cli]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模搜索消耗大量计算资源

## 参考链接

- [https://docs.wandb.ai/guides/sweeps](https://docs.wandb.ai/guides/sweeps)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
