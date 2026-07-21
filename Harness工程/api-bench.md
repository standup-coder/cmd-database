---
{
  "cmd_name": "api-bench",
  "cmd_category": "AI基础设施/Harness工程",
  "cmd_dimension": "Harness工程",
  "cmd_install": "pip install apibench",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tool-bench",
    "swe-bench"
  ],
  "cmd_tags": [
    "evaluation",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/ai/harness-engineering.yaml"
}
---

# api-bench

> APIBench API理解评测，测试LLM理解REST API文档并生成正确调用的能力

## 安装

```bash
pip install apibench
```

## 用法

```
python evaluate.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--api_spec` | API规格文件 |
| `--test_cases` | 测试用例 |

## 示例

### 示例 1: 评测API理解能力

```bash
python evaluate.py --api_spec swagger.json --test_cases tests.json
```

### 示例 2: 指定结果输出文件

```bash
python evaluate.py --api_spec swagger.json --test_cases tests.json --output results.json
```

## 关联命令

- [[tool-bench]]
- [[swe-bench]]

## 风险提示

> ⚠️ **MEDIUM**: 真实API调用需注意

## 参考链接

- [https://github.com/AILab-CVC/APIBench](https://github.com/AILab-CVC/APIBench)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
