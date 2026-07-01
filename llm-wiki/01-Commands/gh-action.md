---
{
  "cmd_name": "gh action",
  "cmd_category": "CI-CD/GitHub Actions",
  "cmd_dimension": "GitHub Actions",
  "cmd_install": "brew install gh (macOS) 或 apt install gh (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gh workflow",
    "gh run"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/cicd/github-actions.yaml"
}
---

# gh action

> 管理 GitHub Actions

## 安装

```bash
brew install gh (macOS) 或 apt install gh (Ubuntu)
```

## 用法

```
gh action list
```

```
gh action enable <action>
```

```
gh action disable <action>
```

## 示例

### 示例 1: 列出仓库中可用的 Actions

```bash
gh action list
```

### 示例 2: 启用指定 Action

```bash
gh action enable my-action
```

## 关联命令

- [[gh workflow]]
- [[gh run]]

## 所属维度

[[GitHub Actions-MOC|CI-CD/GitHub Actions]]
