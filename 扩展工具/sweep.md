---
{
  "cmd_name": "sweep",
  "cmd_category": "AI基础设施/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "pip install sweepai 或 GitHub App",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "swe-agent",
    "aider"
  ],
  "cmd_tags": [
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/ai/llm-extra.yaml"
}
---

# sweep

> AI 驱动的代码 issue 自动修复助手

## 安装

```bash
pip install sweepai 或 GitHub App
```

## 用法

```
sweep [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--issue` | 指定 issue |
| `--repo` | 指定仓库 |
| `--branch` |  |

## 示例

### 示例 1: 根据 issue 生成修复 PR

```bash
sweep --issue 123 --repo myorg/myrepo
```

### 示例 2: 按描述生成修复

```bash
sweep --issue 'Fix memory leak in worker' --repo myorg/myrepo
```

## 关联命令

- [[swe-agent]]
- [[aider]]

## 风险提示

> ⚠️ **HIGH**: AI 自动修改代码可能引入 Bug，请严格审查生成的 PR 并通过 CI

## 所属维度

[[扩展工具-MOC|AI基础设施/扩展工具]]
