---
cmd_name: turbopuffer
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: pip install turbopuffer
cmd_platforms:
- linux
- darwin
- windows
summary: "Turbopuffer高性能托管向量搜索，专为RAG应用优化，支持混合搜索"
cmd_level: intermediate
cmd_related:
- pinecone
- qdrant
cmd_tags:
- application
- rag
- data
- vector-db
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# turbopuffer

> Turbopuffer高性能托管向量搜索，专为RAG应用优化，支持混合搜索

## 安装

```bash
pip install turbopuffer
```

## 用法

```
python app.py (使用turbopuffer库)
```

## 参数

| Flag | Description |
|------|-------------|
| `upsert` | 插入/更新向量 |
| `query` | 查询向量 |

## 示例

### 示例 1: 插入向量

```bash
python -c "import turbopuffer as tp; ns = tp.Namespace('docs'); ns.upsert(ids=['1'], vectors=0.1, attributes={'text':['hello']})"
```

## 关联命令

- [[pinecone]]
- [[qdrant]]

## 风险提示

> ⚠️ **LOW**: 托管服务

## 参考链接

- [https://turbopuffer.com/](https://turbopuffer.com/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
