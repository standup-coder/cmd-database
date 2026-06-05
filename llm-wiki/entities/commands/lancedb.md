---
cmd_name: lancedb
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: pip install lancedb
cmd_platforms:
- linux
- darwin
- windows
summary: "LanceDB无服务器向量数据库，基于Apache Arrow列式存储，支持嵌入和全文搜索"
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


# lancedb

> LanceDB无服务器向量数据库，基于Apache Arrow列式存储，支持嵌入和全文搜索

## 安装

```bash
pip install lancedb
```

## 用法

```
python app.py (使用lancedb库)
```

## 参数

| Flag | Description |
|------|-------------|
| `connect` | 连接数据库 |
| `create_table` | 创建表 |
| `search` | 向量搜索 |

## 示例

### 示例 1: 创建表并插入数据

```bash
python -c "import lancedb; db = lancedb.connect('./lancedb'); tbl = db.create_table('docs', data=[{'vector': [0.1,0.2], 'text': 'hello'}])"
```

### 示例 2: 向量搜索

```bash
python -c "tbl.search([0.1,0.2]).limit(10).to_pandas()"
```

## 关联命令

- [[chroma]]
- [[qdrant]]

## 风险提示

> ⚠️ **LOW**: 轻量级数据库

## 参考链接

- [https://lancedb.github.io/lancedb/](https://lancedb.github.io/lancedb/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
