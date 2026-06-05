---
cmd_name: paddle-lite
cmd_category: AI基础设施/边缘AI
cmd_dimension: 边缘AI
cmd_install: pip install paddlelite
cmd_platforms:
- linux
- darwin
- windows
summary: "Paddle Lite百度端侧推理框架，支持ARM Cortex-M到服务器GPU，极致轻量"
cmd_level: intermediate
cmd_related:
- tflite
- executorch
cmd_tags:
- inference
- edge
- gpu
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/edge-ai.yaml
---


# paddle-lite

> Paddle Lite百度端侧推理框架，支持ARM Cortex-M到服务器GPU，极致轻量

## 安装

```bash
pip install paddlelite
```

## 用法

```
paddle_lite_opt [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model_file` | Paddle模型文件 |
| `--param_file` | 参数文件 |
| `--optimize_out` | 优化输出路径 |
| `--valid_targets` | 目标平台 (arm, opencl, x86) |

## 示例

### 示例 1: ARM端侧优化

```bash
paddle_lite_opt --model_file=model.pdmodel --param_file=model.pdiparams --optimize_out=opt_model --valid_targets=arm
```

### 示例 2: OpenCL GPU优化

```bash
paddle_lite_opt --model_file=model.pdmodel --param_file=model.pdiparams --optimize_out=opt_model --valid_targets=opencl
```

## 关联命令

- [[tflite]]
- [[executorch]]

## 风险提示

> ⚠️ **LOW**: 模型转换安全

## 参考链接

- [https://paddle-lite.readthedocs.io/](https://paddle-lite.readthedocs.io/)

## 所属维度

[[边缘AI-MOC|AI基础设施/边缘AI]]
