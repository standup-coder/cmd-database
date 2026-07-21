---
{
  "cmd_name": "git clone",
  "cmd_category": "版本控制/Git命令",
  "cmd_dimension": "Git命令",
  "cmd_install": "apt install git (Ubuntu) 或 yum install git (CentOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "git pull",
    "git fetch"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/vcs/git.yaml"
}
---

# git clone

> 克隆远程仓库到本地

## 安装

```bash
apt install git (Ubuntu) 或 yum install git (CentOS)
```

## 用法

```
git clone <repository-url> [directory]
```

## 参数

| Flag | Description |
|------|-------------|
| `--depth <n>` | 浅克隆，只克隆最近n次提交 |
| `--branch <name>` | 克隆指定分支 |
| `--single-branch` | 只克隆单个分支 |

## 示例

### 示例 1: 克隆GitHub仓库

```bash
git clone https://github.com/user/repo.git
```

### 示例 2: 浅克隆，只获取最新代码

```bash
git clone --depth 1 https://github.com/user/repo.git
```

## 关联命令

- [[git-pull]]
- [[git-fetch]]

## 所属维度

[[Git命令-MOC|版本控制/Git命令]]
