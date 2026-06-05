---
cmd_name: svn copy
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Create a copy (branch/tag) in repository"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn copy

> Create a copy (branch/tag) in repository

## 安装

```bash
Install Subversion package
```

## 用法

```
svn copy SRC DST -m 'message'
```

## 示例

### 示例 1: Create branch from trunk

```bash
svn copy ^/trunk ^/branches/feature -m 'Create feature branch'
```

### 示例 2: Create tag

```bash
svn copy ^/trunk ^/tags/v1.0 -m 'Tag version 1.0'
```

## 风险提示

> ⚠️ **MEDIUM**: Creates permanent copy in repository

## 所属维度

[[SVN命令-MOC|Version Control]]
