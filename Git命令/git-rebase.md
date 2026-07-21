---
{
  "cmd_name": "git rebase",
  "cmd_category": "版本控制/Git命令",
  "cmd_dimension": "Git命令",
  "cmd_install": "apt install git (Ubuntu) 或 yum install git (CentOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git merge",
    "git cherry-pick",
    "git log"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/vcs/git.yaml"
}
---

# git rebase

> 将当前分支变基到另一分支，重写提交历史

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git rebase [-i | --interactive] [<branch>]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i, --interactive` | 交互式变基，可编辑/合并提交 |
| `--continue` | 解决冲突后继续变基 |
| `--abort` | 中止变基，恢复到变基前状态 |
| `--onto <newbase>` | 将当前分支变基到新基础提交 |

## 示例

### 示例 1: 将当前分支变基到main

```bash
git rebase main
```

### 示例 2: 交互式合并最近3个提交

```bash
git rebase -i HEAD~3
```

## 关联命令

- [[git-merge]]
- [[git-log]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
