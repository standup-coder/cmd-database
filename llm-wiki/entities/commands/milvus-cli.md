---
cmd_name: milvus-cli
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: pip install milvus-cli
cmd_platforms:
- linux
- darwin
- windows
summary: "Milvus分布式向量数据库CLI，支持十亿级向量的高性能ANN搜索"
cmd_level: advanced
cmd_related:
- qdrant
- chroma
cmd_tags:
- data
- vector-db
- distributed
- advanced
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/vector-db.yaml
---


# milvus-cli

> Milvus分布式向量数据库CLI，支持十亿级向量的高性能ANN搜索

## 安装

```bash
pip install milvus-cli
```

## 用法

```
milvus_cli [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `connect` | 连接Milvus服务器 |
| `create collection` | 创建集合 |
| `search` | 向量搜索 |
| `import` | 批量导入数据 |

## 示例

### 示例 1: 连接本地Milvus

```bash
milvus_cli connect --host localhost --port 19530
```

### 示例 2: 创建768维向量集合

```bash
milvus_cli create collection -c my_collection -d 768 -p id
```

### 示例 3: 搜索最近邻

```bash
milvus_cli search -c my_collection -v '[0.1,0.2,...]' -k 10
```

## 关联命令

- [[qdrant]]
- [[chroma]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模数据导入需合理配置资源

## 参考链接

- [https://milvus.io/](https://milvus.io/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
