---
cmd_name: svn cleanup
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Clean up working copy (remove locks, fix interrupted operations)"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn cleanup

> Clean up working copy (remove locks, fix interrupted operations)

## 安装

```bash
Install Subversion package
```

## 用法

```
svn cleanup [PATH]
```

## 示例

### 示例 1: Clean up current directory

```bash
svn cleanup
```

### 示例 2: Clean up specific working copy

```bash
svn cleanup /path/to/workingcopy
```

## 风险提示

> ⚠️ **LOW**: Safe maintenance operation

## 所属维度

[[SVN命令-MOC|Version Control]]
