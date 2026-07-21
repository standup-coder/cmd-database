---
{
  "cmd_name": "livecodebench",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "git clone https://github.com/LiveCodeBench/LiveCodeBench",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "humaneval-exec",
    "swe-bench"
  ],
  "cmd_tags": [
    "evaluation",
    "data",
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# livecodebench

> LiveCodeBench实时代码评测，持续更新的编程题 benchmark，防数据污染，反映模型真实代码能力

## 安装

```bash
git clone https://github.com/LiveCodeBench/LiveCodeBench
```

## 用法

```
python evaluation.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--model` | 评测模型 |
| `--scenario` | 场景 (code_generation, self_repair, test_output) |
| `--release_version` | 评测版本 |

## 示例

### 示例 1: 代码生成能力评测

```bash
python evaluation.py --model gpt-4 --scenario code_generation --release_version v4
```

### 示例 2: 代码自修复能力评测

```bash
python evaluation.py --model claude-3-5-sonnet --scenario self_repair --release_version v5
```

## 关联命令

- [[humaneval-exec]]
- [[swe-bench]]

## 风险提示

> ⚠️ **HIGH**: 执行代码需在隔离环境

## 参考链接

- [https://livecodebench.github.io/](https://livecodebench.github.io/)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
