---
cmd_name: svn revert
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Undo local changes"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn revert

> Undo local changes

## 安装

```bash
Install Subversion package
```

## 用法

```
svn revert PATH
```

## 参数

| Flag | Description |
|------|-------------|
| `-R` | Recursive revert |

## 示例

### 示例 1: Revert changes to file

```bash
svn revert file.txt
```

### 示例 2: Revert all changes recursively

```bash
svn revert -R .
```

## 风险提示

> ⚠️ **HIGH**: Permanently discards uncommitted changes; cannot be undone

## 所属维度

[[SVN命令-MOC|Version Control]]
