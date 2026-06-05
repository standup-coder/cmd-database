---
cmd_name: webdataset
cmd_category: AI基础设施/数据与标注
cmd_dimension: 数据与标注
cmd_install: pip install webdataset
cmd_platforms:
- linux
- darwin
- windows
summary: "WebDataset大规模数据集流式处理库，高效处理TB级训练数据"
cmd_level: advanced
cmd_related:
- datasets-cli
- img2dataset
cmd_tags:
- training
- data
- advanced
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/data-labeling.yaml
---


# webdataset

> WebDataset大规模数据集流式处理库，高效处理TB级训练数据

## 安装

```bash
pip install webdataset
```

## 用法

```
python preprocess.py (使用webdataset库)
```

## 参数

| Flag | Description |
|------|-------------|
| `wds.WebDataset` | 创建数据集管道 |
| `decode` | 解码数据(图像、音频等) |
| `batched` | 批量处理 |

## 示例

### 示例 1: 从tar shards流式加载数据

```bash
python -c "import webdataset as wds; ds = wds.WebDataset('data-{0000..9999}.tar').decode().batched(64)"
```

### 示例 2: 将图像数据打包为WebDataset shards

```bash
python make_shards.py --input_dir ./images --output_pattern shards/data-%06d.tar --shard_size 10000
```

## 关联命令

- [[datasets-cli]]
- [[img2dataset]]

## 风险提示

> ⚠️ **LOW**: 数据处理操作无副作用

## 参考链接

- [https://github.com/webdataset/webdataset](https://github.com/webdataset/webdataset)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
