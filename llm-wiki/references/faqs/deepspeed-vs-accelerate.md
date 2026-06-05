---
faq_question: DeepSpeed 和 Accelerate 怎么选？
faq_tags:
- 训练
- 分布式
- 对比
- intermediate
created: '2026-05-31'
---


# FAQ: DeepSpeed 和 Accelerate 怎么选？

**Q**: DeepSpeed 和 HuggingFace Accelerate 有什么区别？

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

## 关联页面

- [[大模型训练-MOC]]
- [[deepspeed]]
- [[accelerate]]

