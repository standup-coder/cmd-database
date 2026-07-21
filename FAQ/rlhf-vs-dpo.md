---
faq_question: RLHF 和 DPO 有什么区别？
faq_tags:
- 训练
- RLHF
- DPO
- advanced
created: '2026-05-31'
---


# FAQ: RLHF 和 DPO 有什么区别？

**Q**: RLHF、DPO、GRPO 三种偏好优化方法怎么选？

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

## 关联页面

- [[大模型训练-MOC]]
- [[trl]]

