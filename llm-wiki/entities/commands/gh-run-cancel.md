---
cmd_name: gh run cancel
cmd_category: CI-CD/GitHub Actions
cmd_dimension: GitHub Actions
cmd_install: brew install gh (macOS) 或 apt install gh (Ubuntu)
cmd_platforms:
- linux
- darwin
- windows
summary: "取消正在运行的 GitHub Actions 工作流"
cmd_level: intermediate
cmd_related:
- gh run
- gh workflow
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/cicd/github-actions.yaml
---


# gh run cancel

> 取消正在运行的 GitHub Actions 工作流

## 安装

```bash
brew install gh (macOS) 或 apt install gh (Ubuntu)
```

## 用法

```
gh run cancel <run-id>
```

```
gh run cancel --all
```

## 示例

### 示例 1: 取消指定运行

```bash
gh run cancel 12345
```

### 示例 2: 取消所有正在运行的 CI

```bash
gh run cancel --all
```

## 关联命令

- [[gh run]]
- [[gh workflow]]

## 风险提示

> ⚠️ **MEDIUM**: 会中断正在运行的部署流程

## 所属维度

[[GitHub Actions-MOC|CI-CD/GitHub Actions]]
