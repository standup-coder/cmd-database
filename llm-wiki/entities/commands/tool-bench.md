---
cmd_name: tool-bench
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: git clone https://github.com/OpenBMB/ToolBench.git
cmd_platforms:
- linux
- darwin
- windows
summary: "ToolBench工具使用评测基准，16000+ API，测试LLM的工具选择、调用、组合能力"
cmd_level: intermediate
cmd_related:
- api-bench
- agent-bench
cmd_tags:
- evaluation
- intermediate
- linux
- open-source
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# tool-bench

> ToolBench工具使用评测基准，16000+ API，测试LLM的工具选择、调用、组合能力

## 安装

```bash
git clone https://github.com/OpenBMB/ToolBench.git
```

## 用法

```
python inference.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--tool_root_dir` | 工具定义目录 |
| `--model_path` | 模型路径 |

## 示例

### 示例 1: 评测工具使用能力

```bash
python inference.py --tool_root_dir data/toolenv/tools --model_path gpt-4
```

## 关联命令

- [[api-bench]]
- [[agent-bench]]

## 风险提示

> ⚠️ **MEDIUM**: 真实API调用可能产生副作用

## 参考链接

- [https://github.com/OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
