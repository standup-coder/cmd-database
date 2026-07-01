---
{
  "cmd_name": "marqo",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "docker pull marqoai/marqo",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "chroma",
    "qdrant"
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

# marqo

> Marqo端到端向量搜索引擎，内置向量化，零配置语义搜索

## 安装

```bash
docker pull marqoai/marqo
```

## 用法

```
docker run [OPTIONS] marqoai/marqo
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 端口映射 |
| `--name` | 容器名称 |

## 示例

### 示例 1: 启动Marqo服务

```bash
docker run --name marqo -it --privileged -p 8882:8882 marqoai/marqo:latest
```

### 示例 2: Python创建索引

```bash
python -c "import marqo; mq = marqo.Client(url='http://localhost:8882'); mq.create_index('my-index')"
```

## 关联命令

- [[chroma]]
- [[qdrant]]

## 风险提示

> ⚠️ **LOW**: Docker部署安全可控

## 参考链接

- [https://www.marqo.ai/](https://www.marqo.ai/)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
