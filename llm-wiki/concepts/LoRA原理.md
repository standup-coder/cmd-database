---
aliases: ["LoRA (Low-Rank Adaptation)"]
concept_name: "LoRA (Low-Rank Adaptation)"
concept_tags:
  - "训练"
  - "PEFT"
  - "微调"
  - "intermediate"
created: "2026-05-31"
---

# LoRA (Low-Rank Adaptation)

## 什么是 LoRA

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

## 关联页面

- [[大模型训练-MOC]]
- [[peft]]
- [[unsloth]]

