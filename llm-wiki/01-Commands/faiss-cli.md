---
{
  "cmd_name": "faiss-cli",
  "cmd_category": "AI基础设施/向量数据库",
  "cmd_dimension": "向量数据库",
  "cmd_install": "conda install -c pytorch faiss-gpu",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "pgvector",
    "milvus-cli"
  ],
  "cmd_tags": [
    "data",
    "vector-db",
    "gpu",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/vector-db.yaml"
}
---

# faiss-cli

> Facebook AI Similarity Search (FaisS)高性能向量搜索库，支持GPU加速

## 安装

```bash
conda install -c pytorch faiss-gpu
```

## 用法

```
python search.py (使用faiss库)
```

## 参数

| Flag | Description |
|------|-------------|
| `faiss.IndexFlatL2` | 精确L2搜索索引 |
| `faiss.IndexIVFFlat` | 倒排文件近似搜索 |
| `faiss.IndexHNSWFlat` | HNSW图索引 |
| `faiss.index_cpu_to_all_gpus` | 迁移索引到GPU |

## 示例

### 示例 1: 创建索引并搜索最近邻

```bash
python -c "import faiss; index = faiss.IndexFlatL2(768); index.add(vectors); D, I = index.search(query, k=10)"
```

### 示例 2: GPU加速构建IVF索引

```bash
python build_index.py --dim 768 --index_type ivf --nlist 100 --gpu
```

## 关联命令

- [[pgvector]]
- [[milvus-cli]]

## 风险提示

> ⚠️ **LOW**: 库函数调用无副作用

## 参考链接

- [https://github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss)

## 所属维度

[[向量数据库-MOC|AI基础设施/向量数据库]]
