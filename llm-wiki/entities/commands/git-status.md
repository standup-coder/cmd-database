---
cmd_name: git status
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
summary: "显示工作区状态"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/git.yaml
---


# git status

> 显示工作区状态

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git status [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s, --short` | 简短格式输出 |
| `-b, --branch` | 显示分支信息 |

## 示例

### 示例 1: 查看当前状态

```bash
git status
```

### 示例 2: 简短格式显示

```bash
git status -s
```

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
