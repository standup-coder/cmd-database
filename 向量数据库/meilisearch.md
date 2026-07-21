---
{
  "cmd_name": "meilisearch",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "curl -L https://install.meilisearch.com | sh",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "elasticsearch",
    "typesense",
    "vespa-cli"
  ],
  "cmd_tags": [
    "data",
    "vector-db",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# meilisearch

> 开源即时搜索引擎，支持容错搜索和中文分词

## 安装

```bash
curl -L https://install.meilisearch.com | sh
```

## 用法

```
meilisearch [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--master-key` | 设置API主密钥 |
| `--db-path` | 指定数据库路径 |

## 示例

### 示例 1: 带密钥启动搜索服务

```bash
meilisearch --master-key mykey
```

### 示例 2: 搜索文档

```bash
curl -X POST 'http://localhost:7700/indexes/docs/search' -H 'Authorization: Bearer mykey' -d '{"q":"hello"}'
```

## 关联命令

- [[elasticsearch]]
- [[typesense]]
- [[vespa-cli]]

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
