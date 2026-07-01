---
{
  "cmd_name": "img2dataset",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install img2dataset",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "webdataset",
    "datasets-cli"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# img2dataset

> 从URL列表批量下载图像并构建WebDataset格式，支持分布式处理

## 安装

```bash
pip install img2dataset
```

## 用法

```
img2dataset [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--url_list` | URL列表文件(CSV/Parquet) |
| `--output_folder` | 输出目录 |
| `--thread_count` | 下载线程数 |
| `--image_size` | 输出图像尺寸 |
| `--resize_mode` | 调整大小模式 (border, center_crop, no) |

## 示例

### 示例 1: 32线程下载并调整图像为256x256

```bash
img2dataset --url_list urls.csv --output_folder images --thread_count 32 --image_size 256
```

### 示例 2: 构建LAION数据集shards

```bash
img2dataset --url_list laion.parquet --output_folder laion_shards --shard_size 10000 --resize_mode center_crop
```

## 关联命令

- [[webdataset]]
- [[datasets-cli]]

## 风险提示

> ⚠️ **MEDIUM**: 大规模下载可能触发反爬机制，注意版权合规

## 参考链接

- [https://github.com/rom1504/img2dataset](https://github.com/rom1504/img2dataset)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
