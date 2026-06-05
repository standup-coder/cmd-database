---
cmd_name: redisearch
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: docker run redis/redis-stack
cmd_platforms:
- linux
- darwin
- windows
summary: "RediSearch Redis向量搜索模块，支持向量相似性搜索+全文搜索混合查询"
cmd_level: intermediate
cmd_related:
- pgvector
- faiss-cli
cmd_tags:
- data
- vector-db
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# redisearch

> RediSearch Redis向量搜索模块，支持向量相似性搜索+全文搜索混合查询

## 安装

```bash
docker run redis/redis-stack
```

## 用法

```
redis-cli [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `FT.CREATE` | 创建搜索索引 |
| `FT.SEARCH` | 执行搜索 |
| `FT.VECTOR` | 向量字段类型 |

## 示例

### 示例 1: 创建向量搜索索引

```bash
redis-cli FT.CREATE my_idx ON JSON SCHEMA $.embedding AS embedding VECTOR FLAT 6 TYPE FLOAT32 DIM 768 DISTANCE_METRIC COSINE
```

### 示例 2: KNN向量搜索

```bash
redis-cli FT.SEARCH my_idx '*=>[KNN 10 @embedding $vec]' PARAMS 2 vec '[0.1,...]'
```

## 关联命令

- [[pgvector]]
- [[faiss-cli]]

## 风险提示

> ⚠️ **LOW**: Redis部署稳定可靠

## 参考链接

- [https://redis.io/docs/stack/search/](https://redis.io/docs/stack/search/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
