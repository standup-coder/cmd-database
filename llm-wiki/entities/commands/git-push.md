---
cmd_name: git push
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
summary: "推送本地提交到远程仓库"
cmd_level: advanced
cmd_related:
- git pull
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/vcs/git.yaml
---


# git push

> 推送本地提交到远程仓库

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git push [remote] [branch]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u, --set-upstream` | 设置上游分支 |
| `-f, --force` | 强制推送 |
| `--tags` | 推送标签 |

## 示例

### 示例 1: 推送到远程main分支

```bash
git push origin main
```

### 示例 2: 推送并设置上游分支

```bash
git push -u origin feature
```

## 关联命令

- [[git pull]]

## 风险提示

> ⚠️ **HIGH**: 使用--force可能覆盖他人的提交，务必谨慎

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
