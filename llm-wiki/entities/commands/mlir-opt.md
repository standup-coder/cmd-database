---
cmd_name: mlir-opt
cmd_category: AI基础设施/AI编译器
cmd_dimension: AI编译器
cmd_install: pip install mlir-python-bindings
cmd_platforms:
- linux
- darwin
summary: "MLIR中间表示优化器，对计算图进行 lowering、融合、循环变换等编译优化"
cmd_level: advanced
cmd_related:
- iree-compile
- tvmc
cmd_tags:
- compiler
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-compiler.yaml
---


# mlir-opt

> MLIR中间表示优化器，对计算图进行 lowering、融合、循环变换等编译优化

## 安装

```bash
pip install mlir-python-bindings
```

## 用法

```
mlir-opt [OPTIONS] INPUT
```

## 参数

| Flag | Description |
|------|-------------|
| `--pass-pipeline` | 优化管线字符串 |
| `--canonicalize` | 规范化变换 |
| `--cse` | 公共子表达式消除 |
| `--loop-unroll` | 循环展开 |

## 示例

### 示例 1: 规范化+消除冗余+内联优化

```bash
mlir-opt input.mlir --canonicalize --cse --inline -o output.mlir
```

### 示例 2: Linalg方言 lowering 为循环

```bash
mlir-opt input.mlir --pass-pipeline='builtin.module(func.func(convert-linalg-to-loops))' -o lowered.mlir
```

## 关联命令

- [[iree-compile]]
- [[tvmc]]

## 风险提示

> ⚠️ **LOW**: 只读变换不改变原始文件

## 参考链接

- [https://mlir.llvm.org/](https://mlir.llvm.org/)

## 所属维度

[[AI编译器-MOC|AI基础设施/AI编译器]]
