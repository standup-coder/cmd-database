---
title: Wiki Index
tags: ["index", "MOC"]
updated: "2026-07-02"
---

# LLM-Wiki Index

> cmd4coder 大模型领域知识库 — Obsidian Wiki 版  
> *自动维护索引。最后更新: 2026-07-02*

## 统计概览

- **命令实体**: 1112 个 ([[01-Commands/index|浏览全部]])
- **维度分类**: 102 个 MOC 索引 ([[00-Maps/index|浏览全部]])
- **场景分析**: 4 个多轮问答场景 ([[synthesis/index|浏览全部]])
- **概念解释**: 4 个核心概念 ([[concepts/index|浏览全部]])
- **FAQ 问答**: 5 个高频问题 ([[references/faqs/index|浏览全部]])

## 目录索引

| 目录 | 说明 | 索引文件 |
|------|------|----------|
| **00-Maps** | MOC 分类索引 (102 个) | [[00-Maps/index\|MOC 索引总览]] |
| **01-Commands** | 命令详细文档 (1112 个) | [[01-Commands/index\|命令索引]] |
| **02-Scenes** | 场景分析 | [[02-Scenes/index\|场景索引]] |
| **03-Concepts** | 核心概念 | [[03-Concepts/index\|概念索引]] |
| **04-FAQs** | 常见问题 | [[04-FAQs/index\|FAQ 索引]] |
| **05-Troubleshooting** | 故障排查 | [[05-Troubleshooting/index\|排查索引]] |
| **99-Templates** | 页面模板 | [[99-Templates/index\|模板索引]] |
| **best-practices** | 最佳实践指南 (718 个) | [[best-practices/index\|最佳实践索引]] |
| **concepts** | 核心概念解释 (4 个) | [[concepts/index\|概念索引]] |
| **entities** | 结构化实体数据 | [[entities/index\|实体索引]] |
| **references** | FAQ 与参考资料 | [[references/index\|参考资料索引]] |
| **synthesis** | 场景分析与综合 | [[synthesis/index\|场景索引]] |

## 快速导航

### 目录索引

- [[00-Maps/index|MOC 索引]] — 103 个维度分类
- [[01-Commands/index|命令索引]] — 1112 条命令详情
- [[02-Scenes/index|场景索引]] — 多轮问答场景
- [[03-Concepts/index|概念索引]] — 核心概念解释
- [[04-FAQs/index|FAQ 索引]] — 常见问题解答
- [[05-Troubleshooting/index|故障排查索引]] — 问题排查指南
- [[99-Templates/index|模板索引]] — 页面模板

### 按维度

- [[00-Maps/大模型训练-MOC|大模型训练]] — DeepSpeed, Accelerate, Unsloth, GRPO, DPO
- [[00-Maps/大模型推理-MOC|大模型推理]] — vLLM, SGLang, TensorRT-LLM, Ollama
- [[00-Maps/Agent工程-MOC|Agent工程]] — LangChain, AutoGen, DSPy, CrewAI
- [[00-Maps/Harness工程-MOC|评测与Harness]] — SWE-Bench, Arena, LiveCodeBench
- [[00-Maps/AI安全-MOC|AI安全]] — Garak, ModelScan, LLM Guard
- [[00-Maps/AI编译器-MOC|AI编译器]] — TVM, IREE, TensorRT, MLIR
- [[00-Maps/模型可解释性-MOC|模型可解释性]] — SHAP, LIME, Captum
- [[00-Maps/联邦学习-MOC|联邦学习]] — Flower, Opacus, CrypTen

### 按场景

- [[02-Scenes/index|场景索引]] — 查看所有场景
- [[synthesis/scenes/单卡4090微调7B模型|单卡4090微调7B模型]]
- [[synthesis/scenes/生产环境推理部署|生产环境推理部署]]
- [[synthesis/scenes/RAG应用构建|RAG应用构建]]
- [[synthesis/scenes/模型量化与压缩|模型量化与压缩]]

### 核心概念

- [[03-Concepts/index|概念索引]] — 查看所有概念
- [[concepts/ZeRO优化|ZeRO 优化]]
- [[concepts/KV-Cache|KV Cache]]
- [[concepts/推测解码|推测解码]]
- [[concepts/LoRA原理|LoRA 原理]]
- [[concepts/index|查看全部概念...]]

### FAQ 问答

- [[references/faqs/rlhf-vs-dpo|RLHF vs DPO]]
- [[references/faqs/deepspeed-vs-accelerate|DeepSpeed vs Accelerate]]
- [[references/faqs/vllm-vs-sglang|vLLM vs SGLang]]
- [[references/faqs/index|查看全部 FAQ...]]

## 最近活动

- [2026-05-31] INIT — vault 从 cmd4coder YAML 数据转换生成
- [2026-05-31] INGEST — 676 命令页 + 65 MOC + 4 场景 + 4 概念 + 5 FAQ
- [2026-05-31] LINK — 2,071 个 wikilinks，0 损坏

## Dataview 动态列表

```dataview
table cmd_category, cmd_level, cmd_tags
from "entities/commands"
sort cmd_name
limit 20
```

## 元数据

- [[_insights]] — Wiki 结构洞察报告
- [[references/metadata-overview]] — 元数据概览
