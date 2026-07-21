---
aliases: ["KV Cache (Key-Value Cache)"]
concept_name: "KV Cache (Key-Value Cache)"
concept_tags:
  - "推理"
  - "优化"
  - "attention"
  - "intermediate"
created: "2026-05-31"
---

# KV Cache (Key-Value Cache)

## 什么是 KV Cache

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
**A**: 使用 Sliding Window Attention 或 StreamingLLM 限制有效上下文。

## 关联页面

- [[大模型推理-MOC]]
- [[vllm]]
- [[sglang]]

