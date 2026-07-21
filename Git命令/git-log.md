---
{
  "cmd_name": "git log",
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
    "git show",
    "git diff"
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

# git log

> 查看提交历史

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git log [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `--oneline` | 简洁显示（一行） |
| `--graph` | 图形化显示分支 |
| `-n <number>` | 显示最近n次提交 |
| `--author=<name>` | 按作者过滤 |

## 示例

### 示例 1: 查看提交历史

```bash
git log
```

### 示例 2: 图形化显示简洁历史

```bash
git log --oneline --graph
```

### 示例 3: 显示最近10次提交

```bash
git log -n 10
```

## 关联命令

- [[git-show]]
- [[git-diff]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
