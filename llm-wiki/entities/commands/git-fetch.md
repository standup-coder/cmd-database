---
cmd_name: git fetch
cmd_category: 版本控制/Git命令
cmd_dimension: Git命令
cmd_install: apt install git (Ubuntu) 或 yum install git (CentOS)
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- git pull
- git merge
- git clone
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 从远程仓库下载对象和引用，但不合并
created: '2026-06-04'
source_file: data/vcs/git.yaml
---
# git fetch

> 从远程仓库下载对象和引用，但不合并

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git fetch [<remote>] [<refspec>...]
```

## 参数

| Flag | Description |
|------|-------------|
| `--all` | 获取所有远程仓库的更新 |
| `--prune` | 删除远程已不存在的分支跟踪 |
| `--tags` | 获取所有标签 |
| `--depth <n>` | 浅获取，限制历史深度 |

## 示例

### 获取origin远程的最新提交

```bash
git fetch origin
```

### 获取所有远程并清理已删除分支

```bash
git fetch --all --prune
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
