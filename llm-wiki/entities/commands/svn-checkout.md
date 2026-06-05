---
cmd_name: svn checkout
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Check out a working copy from a repository"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn checkout

> Check out a working copy from a repository

## 安装

```bash
Install Subversion package
```

## 用法

```
svn checkout URL [PATH]
```

## 示例

### 示例 1: Checkout repository to local directory

```bash
svn checkout https://svn.example.com/repo/trunk myproject
```

### 示例 2: Checkout specific tag (co is shorthand)

```bash
svn co https://svn.example.com/repo/tags/v1.0
```

## 风险提示

> ⚠️ **LOW**: Downloads repository content; ensure trusted source

## 所属维度

[[SVN命令-MOC|Version Control]]
