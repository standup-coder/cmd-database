---
cmd_name: neo4j-llm
cmd_category: AI基础设施/AI应用
cmd_dimension: AI应用
cmd_install: pip install neo4j langchain-neo4j
cmd_platforms:
- linux
- darwin
- windows
summary: "Neo4j图数据库+LLM知识图谱构建工具，从非结构化文本自动抽取实体关系构建图谱"
cmd_level: intermediate
cmd_related:
- langchain
- llama-index
cmd_tags:
- application
- data
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/ai-applications.yaml
---


# neo4j-llm

> Neo4j图数据库+LLM知识图谱构建工具，从非结构化文本自动抽取实体关系构建图谱

## 安装

```bash
pip install neo4j langchain-neo4j
```

## 用法

```
python kg.py (使用langchain_neo4j库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Neo4jGraph` | 图数据库连接 |
| `GraphCypherQAChain` | Cypher问答链 |

## 示例

### 示例 1: 连接Neo4j图数据库

```bash
python -c "from langchain_neo4j import Neo4jGraph; graph = Neo4jGraph(url='bolt://localhost:7687', username='neo4j', password='password')"
```

### 示例 2: 从文档自动构建知识图谱

```bash
python kg_build.py --docs ./documents/ --schema schema.cypher
```

## 关联命令

- [[langchain]]
- [[llama-index]]

## 风险提示

> ⚠️ **MEDIUM**: 图数据库写入操作需谨慎

## 参考链接

- [https://neo4j.com/labs/genai-ecosystem/](https://neo4j.com/labs/genai-ecosystem/)

## 所属维度

[[AI应用-MOC|AI基础设施/AI应用]]
