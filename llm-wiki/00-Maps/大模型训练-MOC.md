---
{
  "moc_type": "dimension",
  "moc_name": "AI基础设施/大模型训练",
  "moc_order": 0,
  "tags": [
    "MOC",
    "AI",
    "大模型训练"
  ]
}
---

# AI基础设施/大模型训练

> 大语言模型训练与微调工具链，涵盖分布式训练、参数高效微调、量化训练、模型评估

## 命令列表

- 🔴 [[accelerate]] — HuggingFace Accelerate分布式训练配置工具，简化多GPU/TPU训练
- 🟡 [[alpaca-eval]] — 指令跟随能力评估工具，使用GPT-4作为裁判对模型输出进行排序
- 🟡 [[axolotl]] — YAML配置式LLM微调工具，支持LoRA、QLoRA、全参数微调
- 🟡 [[bitsandbytes]] — 8-bit/4-bit量化库，支持QLoRA在消费级GPU上训练大模型
- 🔴 [[cerebras]] — Cerebras Wafer-Scale Engine超大规模AI芯片训练平台，支持十亿到万亿参数模型
- 🔴 [[colossal-ai]] — Colossal-AI统一深度学习加速系统，支持 Gemini、ZeRO、Pipeline 并行
- 🟡 [[composer]] — MosaicML Composer高效训练库，内置100+算法和优化方法
- 🔴 [[deepspeed]] — 微软DeepSpeed大规模分布式训练框架，支持ZeRO优化、3D并行、Offload
- 🟡 [[distilabel]] — Distilabel合成数据生成与模型蒸馏框架，用LLM生成高质量训练数据，支持自对弈和批评
- 🟡 [[dpo]] — DPO (Direct Preference Optimization) 直接偏好优化，无需奖励模型直接从偏好数据微调
- 🟡 [[flash-attn]] — Flash Attention高效注意力实现，2-4倍加速长序列训练，显著降低内存占用
- 🟡 [[grpo]] — GRPO (Group Relative Policy Optimization) 强化学习训练，DeepSeek-R1核心训练方法，无需价值模型
- 🔴 [[lightning]] — PyTorch Lightning高级训练框架，简化分布式训练、混合精度、Checkpoint管理
- 🟡 [[llama-factory]] — LLaMA-Factory一站式大模型微调框架，支持100+模型，预训练/微调/DPO/RLHF全流程
- 🟡 [[llm-factory]] — 一站式LLM训练平台，支持100+模型预训练、微调、RLHF、DPO、量化、推理
- 🟡 [[lm-eval]] — EleutherAI语言模型评估框架，支持HellaSwag、MMLU、ARC等100+基准测试
- 🔴 [[megatron-lm]] — NVIDIA Megatron-LM大规模语言模型训练框架，支持张量/流水线/序列并行
- 🟡 [[mergekit]] — MergeKit模型合并工具，支持SLERP、TIES、DARE、Model Stock等多种合并算法，无需GPU
- 🟡 [[modal]] — Modal Serverless云平台，按需弹性运行AI训练与推理任务
- 🟡 [[mosaicml-streaming]] — MosaicML Streaming高效数据集流式加载，支持多种云存储和Sharding
- 🔴 [[neuronx-nxdt]] — AWS Neuron分布式训练工具，针对Trainium芯片优化的LLM训练
- 🟡 [[opencompass]] — 上海AI Lab开源的模型评测平台，支持50+数据集和多种评测范式
- 🟡 [[peft]] — 参数高效微调库，支持LoRA、QLoRA、IA3、Prompt Tuning等方法
- 🟡 [[torch-titan]] — PyTorch官方原生大模型训练参考实现，支持FSDP2、TP、PP、CP
- 🟡 [[trl]] — Transformers Reinforcement Learning，支持SFT、DPO、PPO、ORPO训练
- 🟡 [[unsloth]] — 2-5倍加速的LLM微调框架，支持LoRA和QLoRA，内存占用减少80%
- 🟡 [[xformers]] — Meta开源的高效Transformer组件库，提供memory_efficient_attention等优化算子

## 统计

- 总命令数: 27
- 维度: 大模型训练
