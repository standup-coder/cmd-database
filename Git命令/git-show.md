---
{
  "cmd_name": "git show",
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
    "git log",
    "git diff",
    "git cat-file"
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

# git show

> 显示提交、标签或对象的详细信息和差异

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git show [<options>] [<object>...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--stat` | 显示修改统计 |
| `--name-only` | 仅显示修改的文件名 |
| `-p` | 显示补丁（默认） |

## 示例

### 示例 1: 显示最新提交的详细信息

```bash
git show HEAD
```

### 示例 2: 显示指定提交的详细信息

```bash
git show abc1234
```

## 关联命令

- [[git log]]
- [[git diff]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
