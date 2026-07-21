---
{
  "cmd_name": "git pull",
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
    "git fetch",
    "git merge"
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

# git pull

> 拉取远程更改并合并

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git pull [remote] [branch]
```

## 参数

| Flag | Description |
|------|-------------|
| `--rebase` | 使用rebase而非merge |
| `--ff-only` | 只允许快进合并 |

## 示例

### 示例 1: 拉取并合并远程更改

```bash
git pull
```

### 示例 2: 拉取并rebase

```bash
git pull --rebase
```

## 关联命令

- [[git-fetch]]
- [[git-merge]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
