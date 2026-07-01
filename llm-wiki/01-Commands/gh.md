---
{
  "cmd_name": "gh",
  "cmd_category": "CI/CD/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://cli.github.com/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git",
    "github-actions"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/cicd/more.yaml"
}
---

# gh

> GitHub 官方 CLI

## 安装

```bash
参考 https://cli.github.com/
```

## 用法

```
gh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `repo` | 仓库 |
| `pr` | Pull Request |
| `issue` |  |
| `workflow` |  |
| `release` |  |

## 示例

### 示例 1: 创建 PR

```bash
gh pr create
```

### 示例 2: 触发 workflow

```bash
gh workflow run ci.yml
```

## 所属维度

[[扩展工具-MOC|CI/CD/扩展工具]]
