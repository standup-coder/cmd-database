---
cmd_name: red-teaming
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: pip install pyrit
cmd_platforms:
- linux
- darwin
- windows
summary: "PyRIT (Python Risk Identification Toolkit) 微软开源红队测试框架，自动化LLM安全测试"
cmd_level: advanced
cmd_related:
- safety-eval
- agent-bench
cmd_tags:
- safety
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# red-teaming

> PyRIT (Python Risk Identification Toolkit) 微软开源红队测试框架，自动化LLM安全测试

## 安装

```bash
pip install pyrit
```

## 用法

```
python red_team.py (使用pyrit库)
```

## 参数

| Flag | Description |
|------|-------------|
| `PromptTarget` | 攻击目标 |
| `Orchestrator` | 编排攻击策略 |
| `Scorer` | 评分结果 |

## 示例

### 示例 1: 树形攻击策略红队测试

```bash
python red_team.py --strategy tree_of_attacks --target gpt-4 --max_depth 5
```

### 示例 2: 批量发送测试提示

```bash
python -c "from pyrit.orchestrator import PromptSendingOrchestrator; o = PromptSendingOrchestrator(prompt_target=target); await o.send_prompts_async(prompt_list=prompts)"
```

## 关联命令

- [[safety-eval]]
- [[agent-bench]]

## 风险提示

> ⚠️ **HIGH**: 红队测试可能触发安全机制，需授权环境

## 参考链接

- [https://github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
