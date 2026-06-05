---
cmd_name: promptfoo
cmd_category: AI基础设施/AI网关
cmd_dimension: AI网关
cmd_install: npm install -g promptfoo
cmd_platforms:
- linux
- darwin
- windows
summary: "Promptfoo Prompt测试与回归框架，CI/CD集成，防止Prompt退化"
cmd_level: intermediate
cmd_related:
- langfuse
- langsmith
cmd_tags:
- gateway
- intermediate
- linux
- open-source
cmd_risk_level: low
created: '2026-05-31'
source_file: data/ai/ai-gateway.yaml
---


# promptfoo

> Promptfoo Prompt测试与回归框架，CI/CD集成，防止Prompt退化

## 安装

```bash
npm install -g promptfoo
```

## 用法

```
promptfoo [COMMAND] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `eval` | 运行评测 |
| `init` | 初始化项目 |
| `share` | 分享结果 |

## 示例

### 示例 1: 初始化Promptfoo项目

```bash
promptfoo init
```

### 示例 2: 运行Prompt回归测试

```bash
promptfoo eval -c promptfooconfig.yaml
```

### 示例 3: 多模型Prompt对比评测

```bash
promptfoo eval --providers openai:gpt-4,anthropic:claude-3 --tests tests.csv
```

## 关联命令

- [[langfuse]]
- [[langsmith]]

## 风险提示

> ⚠️ **LOW**: 测试框架安全

## 参考链接

- [https://www.promptfoo.dev/](https://www.promptfoo.dev/)

## 所属维度

[[AI网关-MOC|AI基础设施/AI网关]]
