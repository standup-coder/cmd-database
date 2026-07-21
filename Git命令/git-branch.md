---
{
  "cmd_name": "git branch",
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
    "git checkout",
    "git switch"
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

# git branch

> 列出、创建或删除分支

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git branch [options] [branch-name]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有分支（包括远程） |
| `-d` | 删除分支 |
| `-D` | 强制删除分支 |
| `-m` | 重命名分支 |

## 示例

### 示例 1: 列出本地分支

```bash
git branch
```

### 示例 2: 创建新分支

```bash
git branch feature-x
```

### 示例 3: 删除已合并的分支

```bash
git branch -d old-feature
```

## 关联命令

- [[git-checkout]]
- [[git-switch]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
