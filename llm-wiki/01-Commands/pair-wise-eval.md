---
{
  "cmd_name": "pair-wise-eval",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install pair-wise-eval",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "arena",
    "mt-bench"
  ],
  "cmd_tags": [
    "evaluation",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# pair-wise-eval

> Pair-wise成对比较评测，ELO评分系统，适用于模型A/B测试和排序

## 安装

```bash
pip install pair-wise-eval
```

## 用法

```
python evaluate.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--comparisons` | 比较结果文件 |
| `--method` | 评分方法 (elo, bradley-terry) |

## 示例

### 示例 1: ELO评分排名

```bash
python evaluate.py --comparisons results.json --method elo
```

### 示例 2: Bootstrap 置信区间排名

```bash
python evaluate.py --comparisons results.json --method bootstrap
```

## 关联命令

- [[arena]]
- [[mt-bench]]

## 风险提示

> ⚠️ **LOW**: 统计分析安全

## 参考链接

- [https://en.wikipedia.org/wiki/Elo_rating_system](https://en.wikipedia.org/wiki/Elo_rating_system)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
