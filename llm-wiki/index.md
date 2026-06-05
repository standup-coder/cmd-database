---
title: Wiki Index
tags: ["index", "MOC"]
updated: "2026-05-31"
---

# LLM-Wiki Index

> cmd4coder 大模型领域知识库 — Obsidian Wiki 版  
> *自动维护索引。最后更新: 2026-05-31*

## 统计概览

- **命令实体**: 676 个 ([[00-Maps/README|浏览全部]])
- **维度分类**: 65 个 MOC 索引
- **场景分析**: 4 个多轮问答场景
- **概念解释**: 4 个核心概念
- **FAQ 问答**: 5 个高频问题

## 快速导航

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

- [[synthesis/scenes/单卡4090微调7B模型|单卡4090微调7B模型]]
- [[synthesis/scenes/生产环境推理部署|生产环境推理部署]]
- [[synthesis/scenes/RAG应用构建|RAG应用构建]]
- [[synthesis/scenes/模型量化与压缩|模型量化与压缩]]

### 核心概念

- [[concepts/ZeRO优化|ZeRO 优化]]
- [[concepts/KV-Cache|KV Cache]]
- [[concepts/推测解码|推测解码]]
- [[concepts/LoRA原理|LoRA 原理]]

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
