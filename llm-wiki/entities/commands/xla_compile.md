---
cmd_name: xla_compile
cmd_category: AI基础设施/AI编译器
cmd_dimension: AI编译器
cmd_install: pip install tensorflow
cmd_platforms:
- linux
- darwin
summary: "TensorFlow XLA(Accelerated Linear Algebra)即时编译，将计算图编译为机器码，TPU训练推理加速"
cmd_level: intermediate
cmd_related:
- tvmc
- trtexec
cmd_tags:
- training
- inference
- compiler
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-compiler.yaml
---


# xla_compile

> TensorFlow XLA(Accelerated Linear Algebra)即时编译，将计算图编译为机器码，TPU训练推理加速

## 安装

```bash
pip install tensorflow
```

## 用法

```
TF_XLA_FLAGS='--tf_xla_auto_jit=2' python train.py
```

## 参数

| Flag | Description |
|------|-------------|
| `TF_XLA_FLAGS` | XLA编译标志 |
| `--tf_xla_auto_jit` | 自动JIT编译级别 (0/1/2) |
| `--tf_xla_cpu_global_jit` | CPU全局JIT |

## 示例

### 示例 1: 全局XLA JIT加速训练

```bash
TF_XLA_FLAGS='--tf_xla_auto_jit=2 --tf_xla_cpu_global_jit' python train.py
```

### 示例 2: 代码中启用XLA

```bash
python -c "import tensorflow as tf; tf.config.optimizer.set_jit(True)"
```

## 关联命令

- [[tvmc]]
- [[trtexec]]

## 风险提示

> ⚠️ **LOW**: JIT编译首次运行较慢

## 参考链接

- [https://www.tensorflow.org/xla](https://www.tensorflow.org/xla)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
