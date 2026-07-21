---
{
  "cmd_name": "big-bench",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "git clone https://github.com/google/BIG-bench.git",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "lm-eval",
    "opencompass"
  ],
  "cmd_tags": [
    "evaluation",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# big-bench

> BIG-bench (Beyond the Imitation Game) 大规模行为评测，200+语言理解任务

## 安装

```bash
git clone https://github.com/google/BIG-bench.git
```

## 用法

```
python bigbench/evaluate_task.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--task` | 任务名称 |
| `--models` | 评测模型列表 |

## 示例

### 示例 1: 评测简单算术任务

```bash
python bigbench/evaluate_task.py --task simple_arithmetic --models gpt-4
```

### 示例 2: 只评测 10 个样例

```bash
python bigbench/evaluate_task.py --task simple_arithmetic --models gpt-4 --max_examples 10
```

## 关联命令

- [[lm-eval]]
- [[opencompass]]

## 风险提示

> ⚠️ **LOW**: 评测操作安全

## 参考链接

- [https://github.com/google/BIG-bench](https://github.com/google/BIG-bench)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
