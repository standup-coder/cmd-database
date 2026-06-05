---
cmd_name: chroma
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: pip install chromadb
cmd_platforms:
- linux
- darwin
- windows
summary: "Chroma轻量级开源向量数据库，专为AI应用设计，易嵌入到Python项目"
cmd_level: intermediate
cmd_related:
- qdrant
- weaviate-cli
cmd_tags:
- application
- data
- vector-db
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# chroma

> Chroma轻量级开源向量数据库，专为AI应用设计，易嵌入到Python项目

## 安装

```bash
pip install chromadb
```

## 用法

```
chroma run [OPTIONS]
```

```
python app.py (使用chromadb库)
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 启动Chroma服务 |
| `--path` | 持久化数据目录 |
| `--port` | 服务端口号 |

## 示例

### 示例 1: 启动Chroma持久化服务

```bash
chroma run --path ./chroma_data --port 8000
```

### 示例 2: Python创建持久化集合

```bash
python -c "import chromadb; client = chromadb.PersistentClient(path='./db'); coll = client.create_collection('docs')"
```

## 关联命令

- [[qdrant]]
- [[weaviate-cli]]

## 风险提示

> ⚠️ **LOW**: 轻量级数据库，风险可控

## 参考链接

- [https://www.trychroma.com/](https://www.trychroma.com/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
