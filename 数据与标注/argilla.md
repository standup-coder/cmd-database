---
{
  "cmd_name": "argilla",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install argilla",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "label-studio",
    "cleanlab"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/data-labeling.yaml"
}
---

# argilla

> Argilla数据标注与质量平台，专注于NLP和LLM数据，支持主动学习工作流

## 安装

```bash
pip install argilla
```

## 用法

```
python app.py (使用argilla库)
```

## 参数

| Flag | Description |
|------|-------------|
| `rg.init` | 初始化Argilla客户端 |
| `rg.Dataset` | 创建数据集 |
| `rg.Record` | 创建记录 |

## 示例

### 示例 1: 连接本地Argilla服务

```bash
python -c "import argilla as rg; rg.init(api_url='http://localhost:6900', api_key='argilla.apikey')"
```

### 示例 2: 上传标注数据到Argilla

```bash
python upload_data.py --dataset sentiment_analysis --file labeled_data.json
```

## 关联命令

- [[label-studio]]
- [[cleanlab]]

## 风险提示

> ⚠️ **LOW**: 标注平台，数据安全需关注

## 参考链接

- [https://argilla.io/](https://argilla.io/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
