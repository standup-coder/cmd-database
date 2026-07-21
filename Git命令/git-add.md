---
{
  "cmd_name": "git add",
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
    "git commit",
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

# git add

> 添加文件到暂存区

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git add <file>...
```

## 参数

| Flag | Description |
|------|-------------|
| `-A, --all` | 添加所有更改 |
| `-p, --patch` | 交互式选择更改部分 |
| `.` | 添加当前目录所有更改 |

## 示例

### 示例 1: 添加单个文件

```bash
git add file.txt
```

### 示例 2: 添加当前目录所有更改

```bash
git add .
```

### 示例 3: 添加所有更改（包括删除）

```bash
git add -A
```

## 关联命令

- [[git-commit]]
- [[git-status]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
