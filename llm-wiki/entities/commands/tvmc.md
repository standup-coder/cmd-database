---
cmd_name: tvmc
cmd_category: AI基础设施/AI编译器
cmd_dimension: AI编译器
cmd_install: pip install apache-tvm
cmd_platforms:
- linux
- darwin
summary: "TVM命令行编译器，将模型编译为高性能机器码，支持ARM/x86/GPU/FPGA多种后端"
cmd_level: intermediate
cmd_related:
- iree-compile
- trtexec
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


# tvmc

> TVM命令行编译器，将模型编译为高性能机器码，支持ARM/x86/GPU/FPGA多种后端

## 安装

```bash
pip install apache-tvm
```

## 用法

```
tvmc [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `compile` | 编译模型 |
| `run` | 运行编译后的模型 |
| `tune` | 自动调优搜索最优算子 |

## 示例

### 示例 1: ONNX模型编译为CPU可执行文件

```bash
tvmc compile model.onnx --target llvm -o model.tar
```

### 示例 2: ONNX模型编译为CUDA后端

```bash
tvmc compile model.onnx --target cuda -o model_cuda.tar
```

### 示例 3: 自动调优搜索1000次最优算子实现

```bash
tvmc tune --target llvm model.onnx --trials 1000 -o tuning_records.json
```

## 关联命令

- [[iree-compile]]
- [[trtexec]]

## 风险提示

> ⚠️ **MEDIUM**: 编译过程消耗大量CPU/GPU资源

## 参考链接

- [https://tvm.apache.org/docs/reference/microtvm/index.html](https://tvm.apache.org/docs/reference/microtvm/index.html)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
