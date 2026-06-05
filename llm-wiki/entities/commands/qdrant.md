---
cmd_name: qdrant
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: docker pull qdrant/qdrant
cmd_platforms:
- linux
- darwin
- windows
summary: "Qdrant高性能开源向量数据库，支持过滤搜索、分布式部署、Rust实现"
cmd_level: advanced
cmd_related:
- milvus-cli
- weaviate-cli
cmd_tags:
- deployment
- data
- vector-db
- distributed
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# qdrant

> Qdrant高性能开源向量数据库，支持过滤搜索、分布式部署、Rust实现

## 安装

```bash
docker pull qdrant/qdrant
```

## 用法

```
docker run [OPTIONS] qdrant/qdrant
```

```
python app.py (使用qdrant-client)
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` | 容器名称 |
| `-p` | 端口映射 |
| `-v` | 数据卷挂载 |

## 示例

### 示例 1: Docker启动Qdrant

```bash
docker run -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
```

### 示例 2: Python客户端连接

```bash
python -c "from qdrant_client import QdrantClient; client = QdrantClient('localhost', port=6333)"
```

## 关联命令

- [[milvus-cli]]
- [[weaviate-cli]]

## 风险提示

> ⚠️ **LOW**: Docker部署安全可控

## 参考链接

- [https://qdrant.tech/](https://qdrant.tech/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
