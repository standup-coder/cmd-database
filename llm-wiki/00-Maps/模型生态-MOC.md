---
moc_type: dimension
moc_name: AI基础设施/模型生态
moc_order: 0
tags:
- MOC
- AI
- 模型生态
---


# AI基础设施/模型生态

> 模型仓库、格式转换与量化工具，覆盖HuggingFace、ModelScope、ONNX等生态

## 命令列表

- 🟡 [[auto-gptq]] — GPTQ后训练量化工具，4-bit量化减少75%显存占用，适合消费级GPU部署
- 🟡 [[autoawq]] — AWQ激活感知的权重量化，4-bit量化精度优于GPTQ，推理速度提升3倍
- 🟡 [[coremltools]] — Apple CoreML模型转换工具，将PyTorch/TensorFlow转换为iOS/macOS原生格式
- 🟡 [[ctranslate2]] — CTranslate2高效推理引擎，支持INT8/INT16/FP16量化，CPU/GPU加速
- 🟡 [[gguf-convert]] — GGUF格式转换工具，将HuggingFace模型转换为llama.cpp兼容格式
- 🟡 [[git-lfs]] — Git Large File Storage，管理大模型权重文件(GB级)的版本控制
- 🟡 [[huggingface-cli]] — HuggingFace Hub命令行工具，支持模型/数据集/Space的上传下载管理
- 🟡 [[mlc-llm]] — MLC LLM全平台大模型部署，支持手机/浏览器/边缘设备/云端
- 🟡 [[model-card]] — 模型卡片(model card)编写规范，记录模型用途、限制、训练数据等元信息
- 🔴 [[model-pruner]] — 模型剪枝工具，移除不重要的权重或神经元，减小模型体积加速推理
- 🟡 [[modelscope]] — 魔搭社区ModelScope命令行工具，国产开源模型仓库管理
- 🟡 [[neuronx-cc]] — AWS Neuron编译器，将PyTorch/TensorFlow模型编译为Trainium/Inferentia高效执行格式
- 🟡 [[optimum-cli]] — HuggingFace Optimum模型优化工具，支持ONNX/TensorRT/OpenVINO导出和量化
- 🟡 [[paddle2onnx]] — PaddlePaddle到ONNX转换工具，支持Paddle模型导出为ONNX格式
- 🟡 [[safetensors-convert]] — Safetensors安全模型格式转换工具，替代pickle防止恶意代码执行
- 🟡 [[tf2onnx]] — TensorFlow到ONNX转换工具，支持SavedModel、Checkpoint、Keras模型

## 统计

- 总命令数: 16
- 维度: 模型生态
