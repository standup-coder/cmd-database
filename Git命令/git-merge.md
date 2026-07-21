---
{
  "cmd_name": "git merge",
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
    "git rebase",
    "git pull"
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

# git merge

> 合并分支

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git merge <branch>
```

## 参数

| Flag | Description |
|------|-------------|
| `--no-ff` | 禁用快进合并 |
| `--squash` | 压缩合并（不创建合并提交） |

## 示例

### 示例 1: 合并feature分支到当前分支

```bash
git merge feature
```

### 示例 2: 非快进合并

```bash
git merge --no-ff feature
```

## 关联命令

- [[git-rebase]]
- [[git-pull]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
