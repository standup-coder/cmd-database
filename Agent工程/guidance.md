---
{
  "cmd_name": "guidance",
  "cmd_category": "AI基础设施/Agent工程",
  "cmd_dimension": "Agent工程",
  "cmd_install": "pip install guidance",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "outlines",
    "instructor"
  ],
  "cmd_tags": [
    "agent",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/ai/agent-engineering.yaml"
}
---

# guidance

> Guidance可控生成库，通过语法约束LLM输出结构，确保JSON/代码格式正确

## 安装

```bash
pip install guidance
```

## 用法

```
python app.py (使用guidance库)
```

## 参数

| Flag | Description |
|------|-------------|
| `guidance()` | 定义生成模板 |
| `gen()` | 受控生成 |
| `select()` | 选择选项 |

## 示例

### 示例 1: 结构化生成计划

```bash
python -c "import guidance; @guidance; def plan(lm): lm += 'Goal: ' + gen('goal') + '\nSteps: ' + gen('steps'); return lm"
```

### 示例 2: Schema约束JSON生成

```bash
python json_gen.py --schema schema.json --model gpt-4
```

## 关联命令

- [[outlines]]
- [[instructor]]

## 风险提示

> ⚠️ **LOW**: 结构化生成降低风险

## 参考链接

- [https://github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance)

## 所属维度

[[Agent工程-MOC|AI基础设施/Agent工程]]
