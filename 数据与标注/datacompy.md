---
{
  "cmd_name": "datacompy",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install datacompy",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "datasets-cli",
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

# datacompy

> 数据集对比工具，比较两个DataFrame的差异，适用于数据验证和回归测试

## 安装

```bash
pip install datacompy
```

## 用法

```
python compare.py (使用datacompy库)
```

## 参数

| Flag | Description |
|------|-------------|
| `datacompy.Compare` | 创建比较对象 |
| `df1` | 第一个DataFrame |
| `df2` | 第二个DataFrame |
| `join_columns` | 连接键列 |

## 示例

### 示例 1: 比较两个DataFrame并生成差异报告

```bash
python -c "import datacompy; comp = datacompy.Compare(df1, df2, join_columns='id'); print(comp.report())"
```

### 示例 2: 查看比较 API 帮助

```bash
python -c "import datacompy; help(datacompy.Compare)"
```

## 关联命令

- [[datasets-cli]]
- [[cleanlab]]

## 风险提示

> ⚠️ **LOW**: 只读对比操作

## 参考链接

- [https://github.com/capitalone/datacompy](https://github.com/capitalone/datacompy)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
