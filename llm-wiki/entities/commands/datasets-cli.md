---
cmd_name: datasets-cli
cmd_category: AI基础设施/数据与标注
cmd_dimension: 数据与标注
cmd_install: pip install datasets
cmd_platforms:
- linux
- darwin
- windows
summary: "HuggingFace Datasets命令行工具，支持数据集下载、加载、转换和发布"
cmd_level: intermediate
cmd_related:
- webdataset
- img2dataset
cmd_tags:
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/data-labeling.yaml
---


# datasets-cli

> HuggingFace Datasets命令行工具，支持数据集下载、加载、转换和发布

## 安装

```bash
pip install datasets
```

## 用法

```
datasets-cli [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `test` | 测试数据集加载 |
| `run-beam` | 在Apache Beam上运行数据集处理 |
| `convert` | 格式转换 |

## 示例

### 示例 1: 加载IMDB数据集

```bash
python -c "from datasets import load_dataset; ds = load_dataset('imdb')"
```

### 示例 2: 流式加载大规模C4数据集

```bash
python -c "from datasets import load_dataset; ds = load_dataset('c4', 'en', streaming=True)"
```

## 关联命令

- [[webdataset]]
- [[img2dataset]]

## 风险提示

> ⚠️ **LOW**: 数据集操作无副作用

## 参考链接

- [https://huggingface.co/docs/datasets](https://huggingface.co/docs/datasets)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
