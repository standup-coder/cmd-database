---
cmd_name: pinecone
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: pip install pinecone-client
cmd_platforms:
- linux
- darwin
- windows
summary: "Pinecone全托管向量数据库，零运维，自动扩缩容"
cmd_level: intermediate
cmd_related:
- chroma
- qdrant
cmd_tags:
- data
- vector-db
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# pinecone

> Pinecone全托管向量数据库，零运维，自动扩缩容

## 安装

```bash
pip install pinecone-client
```

## 用法

```
python app.py (使用pinecone库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Pinecone(api_key=...)` | 初始化客户端 |
| `create_index` | 创建索引 |
| `index.upsert` | 插入向量 |
| `index.query` | 查询向量 |

## 示例

### 示例 1: 查询Pinecone索引

```bash
python -c "from pinecone import Pinecone; pc = Pinecone(api_key='xxx'); index = pc.Index('my-index'); results = index.query(vector=[...], top_k=10)"
```

## 关联命令

- [[chroma]]
- [[qdrant]]

## 风险提示

> ⚠️ **LOW**: 托管服务，注意API费用

## 参考链接

- [https://www.pinecone.io/](https://www.pinecone.io/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
