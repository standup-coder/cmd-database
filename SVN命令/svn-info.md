---
{
  "cmd_name": "svn info",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/vcs/svn.yaml"
}
---

# svn info

> Display information about working copy or repository

## 安装

```bash
Install Subversion package
```

## 用法

```
svn info [PATH]
```

## 示例

### 示例 1: Show working copy information

```bash
svn info
```

### 示例 2: Show repository information

```bash
svn info https://svn.example.com/repo
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[SVN命令-MOC|Version Control]]
