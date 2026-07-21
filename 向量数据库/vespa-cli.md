---
{
  "cmd_name": "vespa-cli",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "brew install vespa-cli",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "milvus-cli",
    "qdrant"
  ],
  "cmd_tags": [
    "inference",
    "data",
    "vector-db",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# vespa-cli

> Vespa大规模搜索与推理引擎，支持向量搜索+结构化搜索+机器学习推理

## 安装

```bash
brew install vespa-cli
```

## 用法

```
vespa [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `deploy` | 部署应用 |
| `feed` | 推送数据 |
| `query` | 执行查询 |
| `status` | 查看状态 |

## 示例

### 示例 1: 部署Vespa应用

```bash
vespa deploy ./application
```

### 示例 2: 向量最近邻搜索

```bash
vespa query 'select * from sources * where {targetHits:10}nearestNeighbor(embedding,q)'
```

## 关联命令

- [[milvus-cli]]
- [[qdrant]]

## 风险提示

> ⚠️ **MEDIUM**: 复杂配置需充分测试

## 参考链接

- [https://vespa.ai/](https://vespa.ai/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
