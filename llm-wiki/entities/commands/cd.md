---
cmd_name: cd
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
summary: "切换当前工作目录"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/os/common.yaml
---


# cd

> 切换当前工作目录

## 用法

```
cd [目录]
```

## 参数

| Flag | Description |
|------|-------------|
| `-` | 切换到上一个工作目录 |
| `~` | 切换到用户主目录 |

## 示例

### 示例 1: 切换到/var/log目录

```bash
cd /var/log
```

### 示例 2: 切换到用户主目录

```bash
cd ~
```

### 示例 3: 切换回上一个目录

```bash
cd -
```

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
