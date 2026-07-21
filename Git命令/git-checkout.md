---
{
  "cmd_name": "git checkout",
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
    "git switch",
    "git restore"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/vcs/git.yaml"
}
---

# git checkout

> 切换分支或恢复文件

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git checkout <branch>
```

```
git checkout <file>
```

## 参数

| Flag | Description |
|------|-------------|
| `-b` | 创建并切换到新分支 |

## 示例

### 示例 1: 切换到main分支

```bash
git checkout main
```

### 示例 2: 创建并切换到新分支

```bash
git checkout -b feature
```

### 示例 3: 恢复文件到最后提交状态

```bash
git checkout -- file.txt
```

## 关联命令

- [[git-switch]]
- [[git-restore]]

## 风险提示

> ⚠️ **MEDIUM**: 恢复文件会丢失未提交的更改

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
