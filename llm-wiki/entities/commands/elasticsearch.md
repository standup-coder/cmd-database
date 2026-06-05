---
cmd_name: elasticsearch
cmd_category: AI基础设施/向量数据库
cmd_dimension: 向量数据库
cmd_install: docker pull elasticsearch:8.x
cmd_platforms:
- linux
- darwin
- windows
summary: "Elasticsearch分布式搜索与分析，8.x版本原生支持dense_vector语义搜索"
cmd_level: advanced
cmd_related:
- opensearch
- vespa-cli
cmd_tags:
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


# elasticsearch

> Elasticsearch分布式搜索与分析，8.x版本原生支持dense_vector语义搜索

## 安装

```bash
docker pull elasticsearch:8.x
```

## 用法

```
docker run [OPTIONS] elasticsearch:8.x
```

## 参数

| Flag | Description |
|------|-------------|
| `--xpack.security.enabled` | 启用/禁用安全 |
| `--discovery.type` | 发现类型 |

## 示例

### 示例 1: 单节点启动(开发)

```bash
docker run -p 9200:9200 -e discovery.type=single-node -e xpack.security.enabled=false elasticsearch:8.12.0
```

## 关联命令

- [[opensearch]]
- [[vespa-cli]]

## 风险提示

> ⚠️ **LOW**: 生产环境需启用安全认证

## 参考链接

- [https://www.elastic.co/](https://www.elastic.co/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
