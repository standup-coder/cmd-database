---
cmd_name: svn status
cmd_category: "版本控制/SVN命令"
cmd_dimension: Version Control
cmd_install: Install Subversion package
cmd_platforms:
- linux
- darwin
- windows
summary: "Show working copy status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/svn.yaml
---


# svn status

> Show working copy status

## 安装

```bash
Install Subversion package
```

## 用法

```
svn status [PATH]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | Show update information |
| `-v` | Verbose output |

## 示例

### 示例 1: Show local changes

```bash
svn status
```

### 示例 2: Show status with update info (st is shorthand)

```bash
svn st -u
```

### 示例 3: Show detailed status

```bash
svn status -v
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[SVN命令-MOC|Version Control]]
