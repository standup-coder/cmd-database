---
{
  "cmd_name": "weaviate-cli",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "docker pull semitechnologies/weaviate",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "qdrant",
    "chroma"
  ],
  "cmd_tags": [
    "data",
    "vector-db",
    "quantization",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# weaviate-cli

> Weaviate AI原生向量数据库，内置向量化和模块化扩展(GraphQL接口)

## 安装

```bash
docker pull semitechnologies/weaviate
```

## 用法

```
docker run [OPTIONS] semitechnologies/weaviate
```

## 参数

| Flag | Description |
|------|-------------|
| `--env QUERY_DEFAULTS_LIMIT` | 默认查询限制 |
| `--env AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED` | 启用匿名访问 |

## 示例

### 示例 1: 启动Weaviate服务

```bash
docker run -p 8080:8080 -p 50051:50051 semitechnologies/weaviate:latest
```

### 示例 2: 查看 Weaviate 容器日志

```bash
docker logs weaviate
```

## 关联命令

- [[qdrant]]
- [[chroma]]

## 风险提示

> ⚠️ **LOW**: Docker部署安全可控

## 参考链接

- [https://weaviate.io/](https://weaviate.io/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
