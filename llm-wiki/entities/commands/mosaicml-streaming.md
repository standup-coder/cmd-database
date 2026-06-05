---
cmd_name: mosaicml-streaming
cmd_category: AI基础设施/大模型训练
cmd_dimension: 大模型训练
cmd_install: pip install streaming
cmd_platforms:
- linux
- darwin
- windows
summary: "MosaicML Streaming高效数据集流式加载，支持多种云存储和Sharding"
cmd_level: intermediate
cmd_related:
- webdataset
- datasets-cli
cmd_tags:
- training
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/llm-training.yaml
---


# mosaicml-streaming

> MosaicML Streaming高效数据集流式加载，支持多种云存储和Sharding

## 安装

```bash
pip install streaming
```

## 用法

```
python convert.py (使用streaming库)
```

## 参数

| Flag | Description |
|------|-------------|
| `StreamingDataset` | 流式数据集类 |
| `writer.MDSWriter` | MDS格式写入器 |

## 示例

### 示例 1: 将数据集转换为MDS格式

```bash
python convert_to_mds.py --input ./raw --output ./mds --splits train val
```

### 示例 2: 从S3流式加载训练数据

```bash
python train.py --dataset_path s3://my-bucket/mds-data
```

## 关联命令

- [[webdataset]]
- [[datasets-cli]]

## 风险提示

> ⚠️ **LOW**: 数据加载工具，风险较低

## 参考链接

- [https://github.com/mosaicml/streaming](https://github.com/mosaicml/streaming)

## 所属维度

[[大模型训练-MOC|AI基础设施/大模型训练]]
