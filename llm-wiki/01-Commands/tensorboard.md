---
{
  "cmd_name": "tensorboard",
  "cmd_category": "AI基础设施/ML框架",
  "cmd_dimension": "ML框架",
  "cmd_install": "pip install tensorboard",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "torchrun"
  ],
  "cmd_tags": [
    "training",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/ml-frameworks.yaml"
}
---

# tensorboard

> TensorFlow和PyTorch的训练可视化工具

## 安装

```bash
pip install tensorboard
```

## 用法

```
tensorboard [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--logdir` | 指定TensorBoard日志文件所在的目录 |
| `--host` | 绑定的主机地址 (默认 'localhost') |
| `--port` | 监听的端口 (默认 6006) |

## 示例

### 示例 1: 启动TensorBoard并读取'runs'目录下的日志

```bash
tensorboard --logdir=runs
```

### 示例 2: 绑定所有 IP 并指定端口

```bash
tensorboard --logdir=runs --host=0.0.0.0 --port=6006
```

## 关联命令

- [[torchrun]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 参考链接

- [https://www.tensorflow.org/tensorboard](https://www.tensorflow.org/tensorboard)

## 所属维度

[[ML框架-MOC|AI基础设施/ML框架]]
