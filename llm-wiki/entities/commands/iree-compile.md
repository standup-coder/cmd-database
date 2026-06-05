---
cmd_name: iree-compile
cmd_category: AI基础设施/AI编译器
cmd_dimension: AI编译器
cmd_install: pip install iree-compiler
cmd_platforms:
- linux
- darwin
summary: "Google IREE MLIR编译器，将深度学习模型编译为Vulkan/SPIR-V/Metal/WebGPU可执行代码"
cmd_level: intermediate
cmd_related:
- tvmc
- mlir-opt
cmd_tags:
- compiler
- gpu
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/ai-compiler.yaml
---


# iree-compile

> Google IREE MLIR编译器，将深度学习模型编译为Vulkan/SPIR-V/Metal/WebGPU可执行代码

## 安装

```bash
pip install iree-compiler
```

## 用法

```
iree-compile [OPTIONS] INPUT -o OUTPUT
```

## 参数

| Flag | Description |
|------|-------------|
| `--iree-hal-target-backends` | 目标后端 (llvm-cpu, vulkan-spirv, cuda) |
| `--iree-input-type` | 输入类型 (mlir, torch, onnx, tflite) |
| `--iree-llvm-target-triple` | LLVM目标三元组 |

## 示例

### 示例 1: MLIR编译为CPU字节码

```bash
iree-compile model.mlir --iree-hal-target-backends=llvm-cpu -o model.vmfb
```

### 示例 2: ONNX编译为Vulkan GPU可执行代码

```bash
iree-compile model.onnx --iree-hal-target-backends=vulkan-spirv --iree-input-type=onnx -o model_gpu.vmfb
```

## 关联命令

- [[tvmc]]
- [[mlir-opt]]

## 风险提示

> ⚠️ **MEDIUM**: 编译过程消耗大量资源

## 参考链接

- [https://iree.dev/](https://iree.dev/)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
