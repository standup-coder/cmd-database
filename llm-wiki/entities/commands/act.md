---
cmd_name: act
cmd_category: CI-CD/GitHub Actions
cmd_dimension: GitHub Actions
cmd_install: brew install act (macOS) 或 curl https://raw.githubusercontent.com/nektos/act/master/install.sh
  | bash
cmd_platforms:
- linux
- darwin
summary: "本地运行 GitHub Actions 工作流（无需推送到 GitHub）"
cmd_level: intermediate
cmd_related:
- gh workflow
- gh run
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/cicd/github-actions.yaml
---


# act

> 本地运行 GitHub Actions 工作流（无需推送到 GitHub）

## 安装

```bash
brew install act (macOS) 或 curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
```

## 用法

```
act [选项]
```

```
act push
```

```
act pull_request
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 仅列出将运行的 Actions |
| `-W` | 指定工作流文件路径 |
| `-e` | 指定事件 JSON 文件 |
| `-v` | 显示详细日志 |
| `-j` | 仅运行指定 Job |

## 示例

### 示例 1: 预览将运行的 Actions

```bash
act -n
```

### 示例 2: 本地模拟 push 事件

```bash
act push
```

### 示例 3: 仅运行 build Job

```bash
act -j build
```

### 示例 4: 运行指定工作流

```bash
act -W .github/workflows/ci.yml
```

## 关联命令

- [[gh workflow]]
- [[gh run]]

## 风险提示

> ⚠️ **MEDIUM**: 本地执行可能暴露 secrets，注意 .secrets 文件

## 所属维度

[[GitHub Actions-MOC|CI-CD/GitHub Actions]]
