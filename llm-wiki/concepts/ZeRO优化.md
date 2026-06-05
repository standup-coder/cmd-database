---
aliases: ["ZeRO (Zero Redundancy Optimizer)"]
concept_name: "ZeRO (Zero Redundancy Optimizer)"
concept_tags:
  - "训练"
  - "分布式"
  - "显存优化"
  - "advanced"
created: "2026-05-31"
---

# ZeRO (Zero Redundancy Optimizer)

## 什么是 ZeRO

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
- FairScale — Meta 的 ZeRO 实现
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

## 关联页面

- [[大模型训练-MOC]]
- [[deepspeed]]

