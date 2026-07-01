---
{
  "cmd_name": "svn delete",
  "cmd_category": "Version Control",
  "cmd_dimension": "Version Control",
  "cmd_install": "Install Subversion package",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/vcs/svn.yaml"
}
---

# svn delete

> Remove files from version control

## 安装

```bash
Install Subversion package
```

## 用法

```
svn delete PATH
```

## 示例

### 示例 1: Delete file from version control

```bash
svn delete oldfile.txt
```

### 示例 2: Delete directory (del is shorthand)

```bash
svn del obsolete/
```

## 风险提示

> ⚠️ **HIGH**: Schedules deletion; file removed from repository after commit

## 所属维度

[[Version Control-MOC|Version Control]]
