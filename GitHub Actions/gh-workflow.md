---
{
  "cmd_name": "gh workflow",
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
    "gh run",
    "gh action"
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

# gh workflow

> 管理 GitHub Actions 工作流

## 安装

```bash
brew install gh (macOS) 或 apt install gh (Ubuntu)
```

## 用法

```
gh workflow list
```

```
gh workflow run <工作流>
```

```
gh workflow view <工作流>
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 指定仓库 (owner/repo) |
| `-f` | 指定触发参数 (-f key=value) |

## 示例

### 示例 1: 列出所有工作流

```bash
gh workflow list
```

### 示例 2: 手动触发工作流并传参

```bash
gh workflow run ci.yml -f branch=main
```

### 示例 3: 查看工作流详情

```bash
gh workflow view ci.yml
```

### 示例 4: 在指定分支触发工作流

```bash
gh workflow run ci.yml --ref feature-branch
```

## 关联命令

- [[gh-run]]
- [[gh-action]]

## 所属维度

[[GitHub Actions-MOC|CI-CD/GitHub Actions]]
