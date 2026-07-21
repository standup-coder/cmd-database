---
faq_question: vLLM 和 SGLang 怎么选？
faq_tags:
- 推理
- 部署
- 对比
- intermediate
created: '2026-05-31'
---


# FAQ: vLLM 和 SGLang 怎么选？

**Q**: vLLM 和 SGLang 有什么区别？

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

## 关联页面

- [[大模型推理-MOC]]
- [[vllm]]
- [[sglang]]

