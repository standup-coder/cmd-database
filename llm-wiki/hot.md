---
title: Hot Cache
updated: "2026-05-31"
tags: ["meta", "hot-cache"]
---

# Hot Cache

*约 500 字的语义快照。每次重大写入操作后更新。*

## Recent Activity

- [2026-05-31] 完成 cmd4coder → LLM-Wiki 全量转换
- 676 命令实体页已生成，覆盖 58 个分类
- 4 个多轮问答场景页就绪
- 2,071 个双向链接，0 损坏

## Active Threads

1. **大模型训练维度** — 27 命令，涵盖 DeepSpeed / Unsloth / GRPO / DPO
2. **大模型推理维度** — 26 命令，涵盖 vLLM / SGLang / TensorRT-LLM
3. **Agent 工程维度** — 19 命令，涵盖 LangChain / AutoGen / DSPy
4. **AI 安全维度** — 5 命令，涵盖 Garak / ModelScan / LLM Guard

## Key Takeaways

- 单卡 4090 可微调 7B 模型（Unsloth + QLoRA）
- vLLM 是生产环境高并发推理首选
- 推测解码可实现 2-3 倍加速而不损失精度
- ZeRO-Offload 可将优化器状态卸载到 CPU

## Flagged Contradictions

*None yet.*
