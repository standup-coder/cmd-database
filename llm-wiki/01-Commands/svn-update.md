---
{
  "cmd_name": "svn update",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/vcs/svn.yaml"
}
---

# svn update

> Update working copy to latest revision

## 安装

```bash
Install Subversion package
```

## 用法

```
svn update [PATH]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | Update to specific revision |

## 示例

### 示例 1: Update to HEAD revision

```bash
svn update
```

### 示例 2: Update to specific revision

```bash
svn update -r 1234
```

### 示例 3: Update specific file (up is shorthand)

```bash
svn up file.txt
```

## 风险提示

> ⚠️ **MEDIUM**: May overwrite local uncommitted changes

## 所属维度

[[Version Control-MOC|Version Control]]
