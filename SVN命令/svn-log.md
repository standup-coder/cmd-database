---
{
  "cmd_name": "svn log",
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

# svn log

> Show commit log messages

## 安装

```bash
Install Subversion package
```

## 用法

```
svn log [PATH]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | Show specific revision range |
| `-v` | Verbose output (show changed paths) |
| `-l` | Limit number of log entries |

## 示例

### 示例 1: Show all commit history

```bash
svn log
```

### 示例 2: Show last 10 commits

```bash
svn log -l 10
```

### 示例 3: Show commits in revision range

```bash
svn log -r 1234:1240
```

### 示例 4: Show detailed history for file

```bash
svn log -v file.txt
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[SVN命令-MOC|Version Control]]
