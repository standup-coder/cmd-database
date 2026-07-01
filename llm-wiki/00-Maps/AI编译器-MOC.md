---
{
  "moc_type": "dimension",
  "moc_name": "AI基础设施/AI编译器",
  "moc_order": 0,
  "tags": [
    "MOC",
    "AI",
    "AI编译器"
  ]
}
---

# AI基础设施/AI编译器

> 模型编译器与推理优化工具，TVM、MLIR、TensorRT、XLA等端到端性能优化

## 命令列表

- 🟡 [[iree-compile]] — Google IREE MLIR编译器，将深度学习模型编译为Vulkan/SPIR-V/Metal/WebGPU可执行代码
- 🔴 [[mlir-opt]] — MLIR中间表示优化器，对计算图进行 lowering、融合、循环变换等编译优化
- 🟡 [[onnx-optimizer]] — ONNX模型图优化器，常量折叠、算子融合、死代码消除，跨平台推理前必备优化
- 🟡 [[trtexec]] — TensorRT引擎构建与性能测试工具，将ONNX/UFF转为TensorRT序列化引擎，极致NVIDIA GPU优化
- 🟡 [[tvmc]] — TVM命令行编译器，将模型编译为高性能机器码，支持ARM/x86/GPU/FPGA多种后端
- 🟡 [[xla_compile]] — TensorFlow XLA(Accelerated Linear Algebra)即时编译，将计算图编译为机器码，TPU训练推理加速

## 统计

- 总命令数: 6
- 维度: AI编译器
