---
{
  "cmd_name": "tensorboard-profiler",
  "cmd_category": "AI基础设施/监控与评估",
  "cmd_dimension": "监控与评估",
  "cmd_install": "pip install tensorboard-plugin-profile",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tensorboard",
    "deepspeed"
  ],
  "cmd_tags": [
    "training",
    "monitoring",
    "gpu",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/monitoring.yaml"
}
---

# tensorboard-profiler

> TensorBoard Profiler性能分析插件，分析模型训练中的CPU/GPU瓶颈

## 安装

```bash
pip install tensorboard-plugin-profile
```

## 用法

```
tensorboard --logdir=logs --bind_all
```

## 参数

| Flag | Description |
|------|-------------|
| `torch.profiler.profile` | PyTorch Profiler配置 |
| `with_stack` | 记录调用栈 |
| `profile_memory` | 分析内存使用 |

## 示例

### 示例 1: 记录训练性能数据

```bash
python profile_train.py --profile --log_dir=logs/profiler
```

### 示例 2: 查看Profiler分析结果

```bash
tensorboard --logdir=logs/profiler --port 6006
```

## 关联命令

- [[tensorboard]]
- [[deepspeed]]

## 风险提示

> ⚠️ **LOW**: 性能分析不改变训练行为

## 参考链接

- [https://www.tensorflow.org/tensorboard/tensorboard_profiling_keras](https://www.tensorflow.org/tensorboard/tensorboard_profiling_keras)

## 所属维度

[[监控与评估-MOC|AI基础设施/监控与评估]]
