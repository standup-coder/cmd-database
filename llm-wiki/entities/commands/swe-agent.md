---
cmd_name: swe-agent
cmd_category: AI基础设施/AI编程
cmd_dimension: AI编程
cmd_install: git clone https://github.com/princeton-nlp/SWE-agent.git && pip install
  -e .
cmd_platforms:
- linux
- darwin
summary: "SWE-Agent自动修复GitHub Issue，分析Issue、编辑代码、运行测试验证修复"
cmd_level: advanced
cmd_related:
- aider
- openhands
cmd_tags:
- agent
- advanced
- linux
- open-source
cmd_risk_level: critical
created: '2026-05-31'
source_file: data/ai/ai-coding.yaml
---


# swe-agent

> SWE-Agent自动修复GitHub Issue，分析Issue、编辑代码、运行测试验证修复

## 安装

```bash
git clone https://github.com/princeton-nlp/SWE-agent.git && pip install -e .
```

## 用法

```
sweagent [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行Agent修复任务 |
| `--agent` | Agent配置 |
| `--model` | 模型名称 |

## 示例

### 示例 1: 自动修复Django Issue

```bash
sweagent run --agent_config config/default.yaml --model_name gpt-4 --data_path https://github.com/django/django/issues/xxxxx
```

### 示例 2: 成本限制内修复Bug

```bash
python run.py --model claude-3-5-sonnet --per_instance_cost_limit 2.00
```

## 关联命令

- [[aider]]
- [[openhands]]

## 风险提示

> ⚠️ **CRITICAL**: 执行真实代码修改，需隔离环境

## 参考链接

- [https://github.com/princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent)

## 所属维度

[[AI编程-MOC|AI基础设施/AI编程]]
