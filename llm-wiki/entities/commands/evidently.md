---
cmd_name: evidently
cmd_category: AI基础设施/数据与标注
cmd_dimension: 数据与标注
cmd_install: pip install evidently
cmd_platforms:
- linux
- darwin
- windows
summary: "Evidently AI模型与数据漂移检测，支持表格数据、NLP、CV全链路监控"
cmd_level: intermediate
cmd_related:
- whylogs
- cleanlab
cmd_tags:
- monitoring
- data
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/data-labeling.yaml
---


# evidently

> Evidently AI模型与数据漂移检测，支持表格数据、NLP、CV全链路监控

## 安装

```bash
pip install evidently
```

## 用法

```
python monitor.py (使用evidently库)
```

## 参数

| Flag | Description |
|------|-------------|
| `Report` | 生成监控报告 |
| `TestSuite` | 运行测试套件 |
| `metrics.DataDriftTable` | 数据漂移指标 |

## 示例

### 示例 1: 生成数据漂移报告

```bash
python -c "from evidently.report import Report; from evidently.metrics import *; r = Report([DataDriftTable()]); r.run(ref, cur); r.save_html('report.html')"
```

### 示例 2: 模型性能监控

```bash
python monitor_model.py --reference ref_data.csv --current cur_data.csv --output dashboard.html
```

## 关联命令

- [[whylogs]]
- [[cleanlab]]

## 风险提示

> ⚠️ **LOW**: 监控分析不改数据

## 参考链接

- [https://evidentlyai.com/](https://evidentlyai.com/)

## 所属维度

[[数据与标注-MOC|AI基础设施/数据与标注]]
