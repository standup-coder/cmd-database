---
cmd_name: git init
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
summary: "初始化新的Git仓库"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/git.yaml
---


# git init

> 初始化新的Git仓库

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git init [directory]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bare` | 创建裸仓库（无工作目录） |

## 示例

### 示例 1: 在当前目录初始化Git仓库

```bash
git init
```

### 示例 2: 创建并初始化新目录

```bash
git init my-project
```

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
