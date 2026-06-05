---
cmd_name: git commit
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
summary: "提交暂存区的更改"
cmd_level: intermediate
cmd_related:
- git add
- git push
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/vcs/git.yaml
---


# git commit

> 提交暂存区的更改

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git commit [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-m <message>` | 指定提交信息 |
| `-a` | 自动暂存已修改的文件 |
| `--amend` | 修改最近一次提交 |

## 示例

### 示例 1: 提交并添加说明

```bash
git commit -m 'Add new feature'
```

### 示例 2: 暂存并提交已修改文件

```bash
git commit -am 'Fix bug'
```

### 示例 3: 修改上次提交

```bash
git commit --amend
```

## 关联命令

- [[git add]]
- [[git push]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
