---
{
  "cmd_name": "svn add",
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

# svn add

> Add files to version control

## 安装

```bash
Install Subversion package
```

## 用法

```
svn add PATH
```

## 示例

### 示例 1: Add single file

```bash
svn add newfile.txt
```

### 示例 2: Add multiple files by pattern

```bash
svn add *.java
```

### 示例 3: Recursively add all unversioned files

```bash
svn add --force .
```

## 风险提示

> ⚠️ **LOW**: Only schedules for addition; not committed until svn commit

## 所属维度

[[Version Control-MOC|Version Control]]
