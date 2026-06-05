---
cmd_name: mbpp
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: pip install datasets
cmd_platforms:
- linux
- darwin
- windows
summary: "MBPP (Mostly Basic Python Programming) 代码生成评测，974个Python编程任务"
cmd_level: advanced
cmd_related:
- humaneval
- ds-1000
cmd_tags:
- evaluation
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# mbpp

> MBPP (Mostly Basic Python Programming) 代码生成评测，974个Python编程任务

## 安装

```bash
pip install datasets
```

## 用法

```
python evaluate.py (使用datasets加载评测)
```

## 参数

| Flag | Description |
|------|-------------|
| `--dataset` | 数据集名称 (mbpp, mbpp_sanitized) |
| `--model_output` | 模型输出文件 |

## 示例

### 示例 1: 评测MBPP数据集

```bash
python evaluate_mbpp.py --dataset mbpp --model_output outputs.json
```

### 示例 2: 加载MBPP数据集

```bash
python -c "from datasets import load_dataset; ds = load_dataset('mbpp')"
```

## 关联命令

- [[humaneval]]
- [[ds-1000]]

## 风险提示

> ⚠️ **HIGH**: 执行模型代码需在沙箱

## 参考链接

- [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
