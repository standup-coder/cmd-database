---
cmd_name: svn switch
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Switch working copy to different URL"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn switch

> Switch working copy to different URL

## 安装

```bash
Install Subversion package
```

## 用法

```
svn switch URL [PATH]
```

## 示例

### 示例 1: Switch to feature branch

```bash
svn switch ^/branches/feature
```

### 示例 2: Switch back to trunk (sw is shorthand)

```bash
svn sw ^/trunk
```

## 风险提示

> ⚠️ **MEDIUM**: Changes working copy location; uncommitted changes may be lost

## 所属维度

[[SVN命令-MOC|Version Control]]
