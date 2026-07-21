---
{
  "cmd_name": "git diff",
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
    "git status",
    "git add",
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

# git diff

> 显示工作区与暂存区或提交之间的差异

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git diff [<options>] [<commit>] [--] [<path>...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--cached` | 显示暂存区与最新提交的差异 |
| `--stat` | 显示统计摘要而非完整差异 |
| `-w` | 忽略空白字符差异 |

## 示例

### 示例 1: 查看未暂存的修改

```bash
git diff
```

### 示例 2: 查看已暂存但未提交的修改

```bash
git diff --cached
```

### 示例 3: 查看最近一次提交的差异

```bash
git diff HEAD~1
```

## 关联命令

- [[git status]]
- [[git add]]
- [[git log]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
