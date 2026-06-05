---
cmd_name: git switch
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- git branch
- git checkout
- git merge
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 切换分支（Git 2.23+ 推荐替代checkout）
created: '2026-06-04'
source_file: data/vcs/git.yaml
---
# git switch

> 切换分支（Git 2.23+ 推荐替代checkout）

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git switch [<options>] [<branch-name>]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c, --create` | 创建并切换到新分支 |
| `-` | 切换到上一个分支 |
| `--detach` | 切换到分离HEAD状态 |

## 示例

### 切换到feature分支

```bash
git switch feature-branch
```

### 创建并切换到新分支

```bash
git switch -c new-feature
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
