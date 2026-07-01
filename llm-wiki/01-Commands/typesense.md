---
{
  "cmd_name": "typesense",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "docker pull typesense/typesense",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "meilisearch",
    "opensearch"
  ],
  "cmd_tags": [
    "data",
    "vector-db",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# typesense

> Typesense开源搜索引擎，支持向量搜索、拼写容错、分面过滤、地理搜索

## 安装

```bash
docker pull typesense/typesense
```

## 用法

```
docker run [OPTIONS] typesense/typesense
```

## 参数

| Flag | Description |
|------|-------------|
| `--data-dir` | 数据目录 |
| `--api-key` | API密钥 |
| `--enable-cors` | 启用CORS |

## 示例

### 示例 1: Docker启动Typesense

```bash
docker run -p 8108:8108 -v /tmp/typesense:/data typesense/typesense:26.0 --data-dir /data --api-key=xyz
```

### 示例 2: 检查 Typesense 健康状态

```bash
docker exec typesense curl http://localhost:8108/health
```

## 关联命令

- [[meilisearch]]
- [[opensearch]]

## 风险提示

> ⚠️ **LOW**: Docker部署安全

## 参考链接

- [https://typesense.org/](https://typesense.org/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
