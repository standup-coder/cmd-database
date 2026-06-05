---
cmd_name: svn diff
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Show differences between revisions"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn diff

> Show differences between revisions

## 安装

```bash
Install Subversion package
```

## 用法

```
svn diff [PATH]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | Compare specific revisions |

## 示例

### 示例 1: Show uncommitted changes

```bash
svn diff
```

### 示例 2: Compare two revisions

```bash
svn diff -r 1234:1235
```

### 示例 3: Show changes in specific file

```bash
svn diff file.txt
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[SVN命令-MOC|Version Control]]
