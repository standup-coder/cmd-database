---
cmd_name: opensearch
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: docker pull opensearchproject/opensearch
cmd_platforms:
- linux
- darwin
- windows
summary: "OpenSearch分布式搜索与分析引擎，支持k-NN向量搜索、ML推理插件"
cmd_level: advanced
cmd_related:
- elasticsearch
- vespa-cli
cmd_tags:
- inference
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


# opensearch

> OpenSearch分布式搜索与分析引擎，支持k-NN向量搜索、ML推理插件

## 安装

```bash
docker pull opensearchproject/opensearch
```

## 用法

```
docker run [OPTIONS] opensearchproject/opensearch
```

## 参数

| Flag | Description |
|------|-------------|
| `--discovery.type` | 发现类型 (single-node) |
| `--plugins.security.disabled` | 禁用安全插件(开发环境) |

## 示例

### 示例 1: 单节点启动OpenSearch

```bash
docker run -p 9200:9200 -e discovery.type=single-node opensearchproject/opensearch:latest
```

### 示例 2: 创建k-NN向量索引

```bash
curl -X PUT localhost:9200/my-index -H 'Content-Type: application/json' -d '{"settings":{"index.knn":true}}'
```

## 关联命令

- [[elasticsearch]]
- [[vespa-cli]]

## 风险提示

> ⚠️ **LOW**: 生产环境需启用安全插件

## 参考链接

- [https://opensearch.org/](https://opensearch.org/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
