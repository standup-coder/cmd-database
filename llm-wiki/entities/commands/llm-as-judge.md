---
cmd_name: llm-as-judge
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: pip install llm-as-judge
cmd_platforms:
- linux
- darwin
- windows
summary: "LLM-as-Judge方法论实现，位置偏见校正、一致性检验、多维度评分"
cmd_level: intermediate
cmd_related:
- prometheus-eval
- judge-eval
cmd_tags:
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# llm-as-judge

> LLM-as-Judge方法论实现，位置偏见校正、一致性检验、多维度评分

## 安装

```bash
pip install llm-as-judge
```

## 用法

```
python judge.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--judge` | 裁判模型 |
| `--swap` | 交换位置检测偏见 |
| `--criteria` | 评分维度 |

## 示例

### 示例 1: 多维度评分并检测位置偏见

```bash
python judge.py --judge gpt-4 --swap --criteria helpfulness,honesty,harmlessness
```

### 示例 2: 计算与人类标注的一致性

```bash
python judge.py --judge prometheus --reference human_labels --compute_agreement
```

## 关联命令

- [[prometheus-eval]]
- [[judge-eval]]

## 风险提示

> ⚠️ **LOW**: 评测框架安全

## 参考链接

- [https://github.com/hemingkx/LLM-as-Judge](https://github.com/hemingkx/LLM-as-Judge)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
