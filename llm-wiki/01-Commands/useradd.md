---
{
  "cmd_name": "useradd",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "usermod",
    "passwd"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# useradd

> 创建用户账户

## 用法

```
useradd [OPTIONS] LOGIN
```

## 参数

| Flag | Description |
|------|-------------|
| `-m` | 创建主目录 |
| `-s` | 指定登录 shell |
| `-G` | 指定附加组 |

## 示例

### 示例 1: 创建用户并生成主目录

```bash
sudo useradd -m -s /bin/bash alice
```

### 示例 2: 创建用户并加入附加组

```bash
sudo useradd -G sudo,adm bob
```

## 关联命令

- [[usermod]]
- [[passwd]]

## 风险提示

> ⚠️ **MEDIUM**: 创建系统用户可能影响权限策略，请确认 UID/GID 范围

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
