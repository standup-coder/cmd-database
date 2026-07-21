---
{
  "cmd_name": "svn commit",
  "cmd_category": "Version Control",
  "cmd_dimension": "Version Control",
  "cmd_install": "Install Subversion package",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/vcs/svn.yaml"
}
---

# svn commit

> Send changes to repository

## 安装

```bash
Install Subversion package
```

## 用法

```
svn commit [PATH] -m 'message'
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | Commit message |
| `-F` | Read commit message from file |

## 示例

### 示例 1: Commit all changes with message

```bash
svn commit -m 'Fix bug in login'
```

### 示例 2: Commit specific file

```bash
svn commit file.txt -m 'Update file'
```

### 示例 3: Commit using shorthand

```bash
svn ci -m 'Add feature'
```

## 风险提示

> ⚠️ **MEDIUM**: Permanently records changes to repository

## 所属维度

[[SVN命令-MOC|Version Control]]
