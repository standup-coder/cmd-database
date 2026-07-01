---
{
  "cmd_name": "whylogs",
  "cmd_category": "AI基础设施/数据与标注",
  "cmd_dimension": "数据与标注",
  "cmd_install": "pip install whylogs",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cleanlab",
    "evidently"
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

# whylogs

> WhyLogs数据日志分析，轻量级数据画像和漂移检测

## 安装

```bash
pip install whylogs
```

## 用法

```
python profile.py (使用whylogs库)
```

## 参数

| Flag | Description |
|------|-------------|
| `why.log` | 记录数据画像 |
| `why.visualize` | 可视化数据画像 |

## 示例

### 示例 1: 生成数据画像

```bash
python -c "import whylogs as why; profile = why.log(pandas=df); profile.view().to_pandas()"
```

### 示例 2: 检测数据漂移

```bash
python drift_monitor.py --reference ref_profile.bin --target target_profile.bin
```

## 关联命令

- [[cleanlab]]
- [[evidently]]

## 风险提示

> ⚠️ **LOW**: 只读分析

## 参考链接

- [https://whylabs.ai/whylogs](https://whylabs.ai/whylogs)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
