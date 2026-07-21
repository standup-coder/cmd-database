---
{
  "cmd_name": "gh run",
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
    "gh run cancel"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/cicd/github-actions.yaml"
}
---

# gh run

> 查看和管理 GitHub Actions 运行记录

## 安装

```bash
brew install gh (macOS) 或 apt install gh (Ubuntu)
```

## 用法

```
gh run list
```

```
gh run view <run-id>
```

```
gh run watch
```

```
gh run rerun <run-id>
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | 指定仓库 |
| `--log` | 查看运行日志 |
| `-b` | 按分支过滤 |
| `-L` | 限制显示数量 |

## 示例

### 示例 1: 查看最近 10 次运行

```bash
gh run list -L 10
```

### 示例 2: 查看运行日志

```bash
gh run view 12345 --log
```

### 示例 3: 实时监控当前运行

```bash
gh run watch
```

### 示例 4: 重新运行失败的 CI

```bash
gh run rerun 12345
```

## 关联命令

- [[gh workflow]]
- [[gh run cancel]]

## 风险提示

> ⚠️ **MEDIUM**: rerun 会消耗 Actions 配额

## 所属维度

[[GitHub Actions-MOC|CI-CD/GitHub Actions]]
