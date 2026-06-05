---
scene_name: 从零构建 RAG 应用
scene_tags:
- RAG
- 应用
- 向量数据库
- 文档解析
- intermediate
scene_difficulty: beginner
created: '2026-05-31'
---


# 场景：从零构建 RAG 应用

## 用户画像

- 有领域文档（PDF、网页、数据库）
- 想构建问答系统
- 需要引用来源、可追溯

## 第一轮：架构设计

**用户**: "我要做一个基于公司文档的问答系统"

**Agent**:

RAG 标准链路：

```
文档 → [[marker]]/[[unstructured]] 解析 → 分块 → [[chroma]]/[[milvus-cli|Milvus]] 存储 → 检索 → LLM 生成
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
| [[milvus-cli|Milvus]] | 分布式、高性能 | 生产环境 |
| Weaviate | 混合搜索 | 多模态 |
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

- Ragas — RAG 专用评测框架
- [[promptfoo]] — Prompt 回归测试
- 人工评测：回答准确率、召回率、引用正确性

## 关联维度

- [[RAG基础设施-MOC]]
- [[向量数据库-MOC]]
- [[langchain]]

