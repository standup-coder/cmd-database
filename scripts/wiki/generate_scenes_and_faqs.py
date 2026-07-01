#!/usr/bin/env python3
"""
Generate Scene pages and FAQ pages for LLM-Wiki
Scenes enable multi-turn QA by providing structured decision trees.
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path("/Users/allengaller/Documents/GitHub/standup-coder/cmd4coder")
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
SCENES_DIR = WIKI_DIR / "02-Scenes"
FAQS_DIR = WIKI_DIR / "04-FAQs"
CONCEPTS_DIR = WIKI_DIR / "03-Concepts"

def write_scene(filename: str, title: str, tags: list, content: str):
    frontmatter = {
        "scene_name": title,
        "scene_tags": tags,
        "scene_difficulty": "beginner",
        "created": "2026-05-31",
    }
    md = f"---\n{json.dumps(frontmatter, ensure_ascii=False, indent=2)}\n---\n\n"
    md += f"# 场景：{title}\n\n"
    md += content
    with open(SCENES_DIR / filename, "w", encoding="utf-8") as f:
        f.write(md)

def write_faq(filename: str, question: str, tags: list, content: str):
    frontmatter = {
        "faq_question": question,
        "faq_tags": tags,
        "created": "2026-05-31",
    }
    md = f"---\n{json.dumps(frontmatter, ensure_ascii=False, indent=2)}\n---\n\n"
    md += f"# FAQ: {question}\n\n"
    md += content
    with open(FAQS_DIR / filename, "w", encoding="utf-8") as f:
        f.write(md)

def write_concept(filename: str, title: str, tags: list, content: str):
    frontmatter = {
        "concept_name": title,
        "concept_tags": tags,
        "created": "2026-05-31",
    }
    md = f"---\n{json.dumps(frontmatter, ensure_ascii=False, indent=2)}\n---\n\n"
    md += f"# {title}\n\n"
    md += content
    with open(CONCEPTS_DIR / filename, "w", encoding="utf-8") as f:
        f.write(md)

def main():
    print("Generating scenes, FAQs, and concepts...")
    
    # === SCENES ===
    
    # Scene 1: 单卡4090微调
    write_scene(
        "单卡4090微调7B模型.md",
        "单卡 RTX 4090 微调 Llama-3-8B",
        ["微调", "LoRA", "单卡", "消费级GPU", "beginner"],
        """## 用户画像

- 只有 1 张 RTX 4090 (24GB)
- 想微调 Llama-3-8B 做领域适配
- 数据量 10K-100K 条

## 第一轮：确认可行性

**用户**: "我只有一张4090，能微调8B模型吗？"

**Agent**:  
可以。8B 模型 FP16 需要 16GB，但微调需要额外显存存优化器状态和梯度。推荐方案：

- [[unsloth]] 4-bit 量化 → 显存降至 ~6GB
- [[qlora]] → 冻结基座只训LoRA适配器
- [[gradient-checkpointing]] → 显存换时间

预估显存占用：**18-20GB**（在 4090 24GB 范围内）。

## 第二轮：工具选择

**用户**: "Unsloth 和 LLaMA-Factory 怎么选？"

**Agent**:

| 维度 | [[unsloth]] | [[llama-factory]] |
|------|-------------|-------------------|
| 速度 | ⭐⭐⭐⭐⭐ 最快 | ⭐⭐⭐ 标准 |
| 易用性 | ⭐⭐⭐⭐ 简单 | ⭐⭐⭐⭐⭐ 最全面 |
| 功能 | LoRA/QLoRA | 全功能预训练/RLHF |
| 推荐 | 快速实验 | 生产环境 |

初学者建议先用 [[unsloth]] 跑通，再迁移到 [[llama-factory]]。

## 第三轮：具体命令

**用户**: "给我具体的命令"

**Agent**:

```bash
# 1. 安装
pip install unsloth

# 2. 训练脚本
python train.py \
  --model_name unsloth/Meta-Llama-3.1-8B-bnb-4bit \
  --max_seq_length 2048 \
  --lora_r 16 \
  --batch_size 2 \
  --gradient_accumulation_steps 4
```

详见 [[unsloth]] 命令页。

## 第四轮：故障排查

**用户**: "训练到一半报 OOM 了"

**Agent**:

诊断路径：
1. 检查 max_seq_length 是否过大 → 降至 1024
2. 启用 [[gradient-checkpointing]] → 显存减半
3. 减小 lora_r → 8 或 4
4. 使用 [[deepspeed]] ZeRO-Offload 将优化器状态放到 CPU

```bash
deepspeed train.py --deepspeed ds_config_zero2_offload.json
```

## 第五轮：部署推理

**用户**: "微调完了怎么部署推理？"

**Agent**:

推荐 [[vllm]] 或 [[ollama]]：

```bash
# 合并 LoRA 权重
llamafactory-cli export --model_dir ./sft_model --export_dir ./merged

# vLLM 部署
python -m vllm.entrypoints.openai.api_server --model ./merged
```

继续 → [[生产环境推理部署]] 场景
"""
    )
    
    # Scene 2: 生产环境推理部署
    write_scene(
        "生产环境推理部署.md",
        "生产环境大模型推理部署",
        ["推理", "部署", "生产环境", "vLLM", "intermediate"],
        """## 用户画像

- 模型已训练/微调完成
- 需要对外提供 API 服务
- 要求高并发、低延迟、高可用

## 第一轮：架构选型

**用户**: "我要部署一个7B模型提供API服务，怎么选？"

**Agent**:

| 场景 | 推荐方案 | 并发 | 延迟 |
|------|----------|------|------|
| 高并发 GPU 集群 | [[vllm]] | 1000+ req/s | <50ms |
| 单卡快速部署 | [[sglang]] | 100+ req/s | <30ms |
| 本地开发测试 | [[ollama]] | 10 req/s | <100ms |
| 边缘设备 | [[llama.cpp]] | 1-5 req/s | 可变 |
| 云托管免运维 | [[together]] / [[fireworks]] | 无限 | <100ms |

## 第二轮：vLLM 部署

**用户**: "我选 vLLM，具体怎么部署？"

**Agent**:

```bash
# 单卡启动
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3-8B-Instruct \
  --tensor-parallel-size 1 \
  --max-num-seqs 256

# 多卡 Tensor Parallel
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3-70B-Instruct \
  --tensor-parallel-size 4
```

详见 [[vllm]] 命令页。

## 第三轮：API 网关

**用户**: "需要限流、监控、多模型路由"

**Agent**:

推荐 [[helicone]] 或 [[portkey]]：

```python
# Helicone 代理
client = openai.OpenAI(
    api_key="sk-xxx",
    base_url="https://oai.hconeai.com/v1"
)
```

功能：语义缓存、成本追踪、A/B测试、Fallback。

## 第四轮：监控

**用户**: "怎么监控模型性能和成本？"

**Agent**:

- [[langfuse]] — LLM 应用可观测性
- [[phoenix]] — Arize AI 开源版
- [[helicone]] — 内置成本分析

## 第五轮：安全

**用户**: "怎么防止Prompt注入和滥用？"

**Agent**:

- [[llm-guard]] — 输入输出安全过滤
- [[garak]] — 定期漏洞扫描
- [[kong-ai-gateway]] — 企业级访问控制
"""
    )
    
    # Scene 3: RAG应用构建
    write_scene(
        "RAG应用构建.md",
        "从零构建 RAG 应用",
        ["RAG", "应用", "向量数据库", "文档解析", "intermediate"],
        """## 用户画像

- 有领域文档（PDF、网页、数据库）
- 想构建问答系统
- 需要引用来源、可追溯

## 第一轮：架构设计

**用户**: "我要做一个基于公司文档的问答系统"

**Agent**:

RAG 标准链路：

```
文档 → [[marker]]/[[unstructured]] 解析 → 分块 → [[chroma]]/[[milvus]] 存储 → 检索 → LLM 生成
```

## 第二轮：文档解析

**用户**: "文档是PDF格式的，怎么解析？"

**Agent**:

| 工具 | 优势 | 适用 |
|------|------|------|
| [[marker]] | 表格/公式准确 | 学术论文 |
| [[docling]] | 结构保留好 | 技术文档 |
| [[llamaparse]] | 云端、高质量 | 批量处理 |
| [[unstructured]] | 50+格式 | 混合来源 |

```bash
marker ./pdfs ./markdown --workers 4
```

## 第三轮：向量存储

**用户**: "选哪个向量数据库？"

**Agent**:

| 工具 | 特点 | 适用 |
|------|------|------|
| [[chroma]] | 轻量、嵌入式 | 原型/小项目 |
| [[milvus]] | 分布式、高性能 | 生产环境 |
| [[weaviate]] | 混合搜索 | 多模态 |
| [[pinecone]] | 全托管 | 免运维 |

## 第四轮：Agent 编排

**用户**: "怎么把 RAG 和 Agent 结合？"

**Agent**:

- [[langchain]] — 最成熟的 RAG 框架
- [[llama-index]] — 高级检索策略
- [[dify]] — 可视化工作流
- [[dspy]] — 声明式优化

## 第五轮：评测

**用户**: "怎么评估 RAG 效果？"

**Agent**:

- [[ragas]] — RAG 专用评测框架
- [[promptfoo]] — Prompt 回归测试
- 人工评测：回答准确率、召回率、引用正确性
"""
    )
    
    # Scene 4: 模型量化与压缩
    write_scene(
        "模型量化与压缩.md",
        "大模型量化与端侧部署",
        ["量化", "压缩", "边缘AI", "推理优化", "advanced"],
        """## 用户画像

- 模型太大，推理成本太高
- 需要在边缘设备运行
- 可以接受少量精度损失

## 第一轮：量化方案选择

**用户**: "我想把70B模型量化到能在单卡运行"

**Agent**:

| 量化方法 | 精度损失 | 显存节省 | 速度提升 | 工具 |
|----------|----------|----------|----------|------|
| INT8 | <1% | 2x | 1.5x | [[onnxruntime]] |
| GPTQ 4-bit | 1-3% | 4x | 2x | [[auto-gptq]] |
| AWQ 4-bit | <1% | 4x | 2.5x | [[auto-awq]] |
| GGUF Q4_K_M | 1-2% | 4x | 2x | [[llama.cpp]] |
| GGUF Q5_K_M | <1% | 3.2x | 1.8x | [[llama.cpp]] |

## 第二轮：AWQ 量化

**用户**: "我选 AWQ，怎么操作？"

**Agent**:

```bash
# AutoAWQ 量化
python -c "
from awq import AutoAWQForCausalLM
model = AutoAWQForCausalLM.from_pretrained('meta-llama/Llama-3-70B')
model.quantize(tokenizer, quant_config={'zero_point': True, 'q_group_size': 128})
model.save_quantized('llama-3-70b-awq')
"
```

## 第三轮：编译器优化

**用户**: "量化后怎么进一步加速？"

**Agent**:

- [[tensorrt-llm]] — NVIDIA GPU 极致优化
- [[tvmc]] — 跨平台编译（ARM/移动端）
- [[iree-compile]] — Vulkan/SPIR-V GPU

```bash
trtexec --onnx=model.onnx --saveEngine=model.trt --fp16 --int8
```

## 第四轮：端侧部署

**用户**: "我想在手机/嵌入式设备运行"

**Agent**:

- [[tflite]] — Android/iOS
- [[executorch]] — PyTorch 移动端
- [[mediapipe]] — Google 端侧流水线
- [[llama.cpp]] — 任何有 C++ 编译器的设备
"""
    )
    
    # === FAQS ===
    
    write_faq(
        "单卡4090能训练多大模型.md",
        "单卡 RTX 4090 能训练多大的模型？",
        ["训练", "显存", "4090", "beginner"],
        """**Q**: 单卡 RTX 4090 (24GB) 能训练多大的 LLM？

**A**: 取决于精度和优化策略：

| 精度 | 优化 | 最大模型 | 推荐工具 |
|------|------|----------|----------|
| FP16 | 无 | 3B | [[transformers-cli]] |
| FP16 | Gradient Checkpointing | 7B | [[accelerate]] |
| INT8 | LoRA | 13B | [[peft]] |
| NF4 (QLoRA) | Unsloth | 70B | [[unsloth]] |

详细方案见 [[单卡4090微调7B模型]] 场景页。

**追问1**: QLoRA 会损失多少精度？  
**A**: 通常 < 1% 性能损失，详见 [[qlora]] 命令页。

**追问2**: 70B 量化后推理速度如何？  
**A**: 使用 [[vllm]] batch 推理可达 20 tokens/s。
"""
    )
    
    write_faq(
        "deepspeed-vs-accelerate.md",
        "DeepSpeed 和 Accelerate 怎么选？",
        ["训练", "分布式", "对比", "intermediate"],
        """**Q**: DeepSpeed 和 HuggingFace Accelerate 有什么区别？

**A**:

| 维度 | [[deepspeed]] | [[accelerate]] |
|------|---------------|----------------|
| 定位 | 极致性能优化 | 简化分布式配置 |
| ZeRO | ZeRO-1/2/3/Offload | 简化版 |
| 3D并行 | ✅ 数据+模型+流水线 | ❌ |
| 学习曲线 | 陡峭 | 平缓 |
| 适用 | 超大规模预训练 | 快速实验/微调 |

**建议**：
- 单卡/小规模 → [[accelerate]]
- 7B 以上多卡 → [[deepspeed]]
- 70B+ 预训练 → [[deepspeed]] + [[megatron-lm]]
"""
    )
    
    write_faq(
        "vllm-vs-sglang.md",
        "vLLM 和 SGLang 怎么选？",
        ["推理", "部署", "对比", "intermediate"],
        """**Q**: vLLM 和 SGLang 有什么区别？

**A**:

| 维度 | [[vllm]] | [[sglang]] |
|------|----------|------------|
| 核心技术 | PagedAttention | RadixAttention |
| 吞吐量 | 极高 | 极高 |
| 延迟 | 低 | 更低 |
| 编程模型 | OpenAI API | Structured Generation |
| 生态 | 更成熟 | 更灵活 |

**建议**：
- 标准 API 服务 → [[vllm]]
- 结构化输出/复杂工作流 → [[sglang]]
- 两者都支持 [[speculative-decoding]] 和 [[prefix-caching]]
"""
    )
    
    write_faq(
        "rlhf-vs-dpo.md",
        "RLHF 和 DPO 有什么区别？",
        ["训练", "RLHF", "DPO", "advanced"],
        """**Q**: RLHF、DPO、GRPO 三种偏好优化方法怎么选？

**A**:

| 方法 | 奖励模型 | 稳定性 | 效果 | 工具 |
|------|----------|--------|------|------|
| RLHF (PPO) | 需要 | 低 | 好 | [[trl]] |
| DPO | 不需要 | 中 | 好 | [[trl]] |
| GRPO | 不需要 | 中 | 很好 | [[trl]] |
| KTO | 不需要 | 高 | 好 | [[trl]] |

**演进路线**：
1. SFT 监督微调
2. DPO 直接偏好优化（无需奖励模型，推荐入门）
3. GRPO 组相对策略优化（DeepSeek-R1 核心方法）

详见 [[dpo]]、[[grpo]]、[[trl]] 命令页。
"""
    )
    
    write_faq(
        "模型安全扫描.md",
        "怎么对 LLM 进行安全扫描？",
        ["安全", "评测", "intermediate"],
        """**Q**: 部署前需要对 LLM 做哪些安全检查？

**A**: 三层安全检查：

**1. 模型文件安全**
- [[modelscan]] — 扫描 Pickle/模型文件恶意代码

**2. 输入输出安全**
- [[llm-guard]] — 过滤 PII 泄露、毒性、越狱
- [[garak]] — 探测提示注入、数据泄露

**3. 红队测试**
- [[red-teaming]] — 系统性对抗攻击测试
- [[safety-eval]] — 毒性/偏见/隐私评测

```bash
# 快速安全检查清单
garak --model_type openai --model_name gpt-4 --probes all
modelscan /path/to/models/
```
"""
    )
    
    # === CONCEPTS ===
    
    write_concept(
        "ZeRO优化.md",
        "ZeRO (Zero Redundancy Optimizer)",
        ["训练", "分布式", "显存优化", "advanced"],
        """## 什么是 ZeRO

ZeRO 是微软提出的显存优化技术，将 optimizer states、gradients、parameters 分片到不同 GPU，消除数据并行中的冗余存储。

## ZeRO 三个阶段

| 阶段 | 优化内容 | 显存节省 | 通信量 |
|------|----------|----------|--------|
| ZeRO-1 | Optimizer States 分片 | 4x | 1x |
| ZeRO-2 | + Gradients 分片 | 8x | 1x |
| ZeRO-3 | + Parameters 分片 | 与数据并行度线性相关 | 1.5x |

## ZeRO-Offload

将 optimizer states 和计算卸载到 CPU/NVMe：

| 配置 | 单卡显存 | 适用 |
|------|----------|------|
| ZeRO-2 | ~1.5x 模型大小 | 7B-13B |
| ZeRO-3 | ~1x 模型大小 | 13B-70B |
| ZeRO-Offload | ~0.5x 模型大小 | 任何规模 |

## 工具支持

- [[deepspeed]] — 最完整的 ZeRO 实现
- [[fairscale]] — Meta 的 ZeRO 实现
- [[torch-titan]] — PyTorch 原生 ZeRO

## 配置示例

```json
{
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": { "device": "cpu" },
    "offload_param": { "device": "cpu" }
  }
}
```
"""
    )
    
    write_concept(
        "KV-Cache.md",
        "KV Cache (Key-Value Cache)",
        ["推理", "优化", "attention", "intermediate"],
        """## 什么是 KV Cache

Transformer 自回归生成时，每个新 token 的计算需要所有历史 token 的 Key 和 Value。KV Cache 缓存这些中间结果，避免重复计算。

## 显存占用公式

```
KV Cache = 2 × num_layers × num_heads × head_dim × seq_len × batch_size × dtype_size

# Llama-3-8B 示例
= 2 × 32 × 128 × 128 × 8192 × 1 × 2  (FP16)
= ~16 GB
```

## 优化技术

| 技术 | 原理 | 工具 |
|------|------|------|
| [[prefix-caching]] | 复用共享前缀 | [[vllm]], [[sglang]] |
| KV Cache 量化 | INT8/FP8 压缩 | [[vllm]] |
| Multi-Query Attention | 共享 KV | 模型架构 |
| Grouped-Query Attention | 分组共享 | Llama-3 |

## 常见问题

**Q**: 为什么长文本推理会 OOM？  
**A**: KV Cache 随序列长度线性增长。128K 上下文可能需要 100GB+ 显存。

**Q**: 怎么减少 KV Cache？  
**A**: 使用 [[sliding-window-attention]] 或 [[streaming-llm]] 限制有效上下文。
"""
    )
    
    write_concept(
        "推测解码.md",
        "Speculative Decoding",
        ["推理", "加速", "advanced"],
        """## 什么是推测解码

用小模型（草稿模型）快速生成候选 token，大模型（目标模型）并行验证，接受正确token、拒绝错误token。实现 2-3 倍加速而不损失精度。

## 原理

```
草稿模型: 小模型 → token_1, token_2, token_3, token_4, token_5
目标模型: 大模型 → 并行验证5个token
          → 接受前3个，拒绝第4个
          → 重新从第4个开始
```

## 关键参数

| 参数 | 说明 | 典型值 |
|------|------|--------|
| `num_assistant_tokens` | 每次推测数 | 3-5 |
| 草稿模型大小 | 通常为目标的 1/10 | TinyLlama-1.1B |

## 工具支持

- [[vllm]] — `--speculative-model`
- [[sglang]] — 内置支持
- [[transformers-cli]] — `assistant_model` 参数

## 适用场景

- 大模型 + 小模型组合（如 Llama-70B + TinyLlama）
- 批处理场景（单请求加速效果有限）
- 对延迟敏感的生产环境
"""
    )
    
    write_concept(
        "LoRA原理.md",
        "LoRA (Low-Rank Adaptation)",
        ["训练", "PEFT", "微调", "intermediate"],
        """## 什么是 LoRA

LoRA 冻结预训练模型的权重，只训练低秩分解矩阵来注入领域知识。将参数更新量 ΔW 分解为两个低秩矩阵 A × B。

## 公式

```
h = W_0 × x + ΔW × x
   = W_0 × x + B × A × x

其中:
- W_0: 冻结的预训练权重 (d × d)
- B: d × r 矩阵
- A: r × d 矩阵
- r << d (rank, 通常为 8-64)
```

## 显存对比

| 方法 | 可训练参数 | 7B模型显存 |
|------|-----------|-----------|
| 全参数微调 | 7B | ~80GB |
| LoRA (r=16) | ~35M (0.5%) | ~20GB |
| QLoRA (4-bit) | ~35M | ~10GB |

## 变体

| 变体 | 特点 | 适用 |
|------|------|------|
| LoRA | 标准低秩 | 通用 |
| QLoRA | 4-bit量化基座 | 消费级GPU |
| DoRA | 权重分解 | 更高精度 |
| LoRA-FA | 冻结A只训B | 更快收敛 |

## 工具

- [[peft]] — HuggingFace LoRA 库
- [[unsloth]] — 极速 LoRA 训练
- [[llama-factory]] — 一站式 LoRA 微调
"""
    )
    
    print(f"Done!")
    print(f"  Scenes:     {len(list(SCENES_DIR.glob('*.md')))}")
    print(f"  FAQs:       {len(list(FAQS_DIR.glob('*.md')))}")
    print(f"  Concepts:   {len(list(CONCEPTS_DIR.glob('*.md')))}")

if __name__ == "__main__":
    main()
