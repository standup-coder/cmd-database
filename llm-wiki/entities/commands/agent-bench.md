---
cmd_name: agent-bench
cmd_category: AI基础设施/Harness工程
cmd_dimension: Harness工程
cmd_install: git clone https://github.com/THUDM/AgentBench.git
cmd_platforms:
- linux
- darwin
summary: "AgentBench多场景Agent能力评测，涵盖OS、数据库、知识图谱、数字卡牌、网页浏览"
cmd_level: advanced
cmd_related:
- swe-bench
- tool-bench
cmd_tags:
- evaluation
- agent
- data
- advanced
- linux
- open-source
cmd_risk_level: high
created: '2026-05-31'
source_file: data/ai/harness-engineering.yaml
---


# agent-bench

> AgentBench多场景Agent能力评测，涵盖OS、数据库、知识图谱、数字卡牌、网页浏览

## 安装

```bash
git clone https://github.com/THUDM/AgentBench.git
```

## 用法

```
python eval.py [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--task` | 评测任务 (os, db, kg, card, web) |
| `--agent` | Agent配置文件 |

## 示例

### 示例 1: 评测OS操作Agent

```bash
python eval.py --task os --agent configs/gpt-4.yaml
```

### 示例 2: 全场景Agent评测

```bash
python eval.py --task all --agent configs/claude-3.yaml
```

## 关联命令

- [[swe-bench]]
- [[tool-bench]]

## 风险提示

> ⚠️ **HIGH**: OS任务Agent可能执行系统命令，需隔离环境

## 参考链接

- [https://github.com/THUDM/AgentBench](https://github.com/THUDM/AgentBench)

## 所属维度

[[Harness工程-MOC|AI基础设施/Harness工程]]
