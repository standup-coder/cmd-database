---
{
  "cmd_name": "git restore",
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
    "git reset",
    "git status"
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

# git restore

> 恢复工作区或暂存区文件（Git 2.23+ 推荐替代checkout）

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git restore [<options>] [<pathspec>...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--staged` | 恢复暂存区中的文件 |
| `--source <tree>` | 从指定提交恢复文件 |
| `--worktree` | 恢复工作区文件（默认） |

## 示例

### 示例 1: 撤销对file.txt的修改

```bash
git restore file.txt
```

### 示例 2: 取消暂存file.txt

```bash
git restore --staged file.txt
```

## 关联命令

- [[git-checkout]]
- [[git-status]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
