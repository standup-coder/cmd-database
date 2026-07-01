---
{
  "cmd_name": "pgvector",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "CREATE EXTENSION vector; (PostgreSQL扩展)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "milvus-cli",
    "chroma"
  ],
  "cmd_tags": [
    "data",
    "vector-db",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# pgvector

> pgvector PostgreSQL向量扩展，在关系数据库中直接存储和查询向量

## 安装

```bash
CREATE EXTENSION vector; (PostgreSQL扩展)
```

## 用法

```
psql -c [SQL]
```

## 参数

| Flag | Description |
|------|-------------|
| `CREATE EXTENSION vector` | 启用扩展 |
| `CREATE TABLE ... (embedding vector(768))` | 创建含向量列的表 |
| `SELECT ... ORDER BY embedding <-> query_embedding LIMIT 10` | L2距离向量搜索 |

## 示例

### 示例 1: 在PostgreSQL中启用pgvector

```bash
psql -c 'CREATE EXTENSION vector'
```

### 示例 2: 创建向量表和余弦相似度索引

```bash
psql -c "CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(768)); CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops)"
```

## 关联命令

- [[milvus-cli]]
- [[chroma]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模向量索引构建可能耗时

## 参考链接

- [https://github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
