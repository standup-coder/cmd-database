---
{
  "cmd_name": "userdel",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "useradd",
    "usermod"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# userdel

> 删除用户账户

## 用法

```
userdel [OPTIONS] LOGIN
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 同时删除主目录和邮件池 |
| `-f` | 强制删除 |

## 示例

### 示例 1: 删除用户

```bash
sudo userdel alice
```

### 示例 2: 删除用户及其主目录

```bash
sudo userdel -r alice
```

## 关联命令

- [[useradd]]
- [[usermod]]

## 风险提示

> ⚠️ **HIGH**: 删除用户及其主目录会丢失数据，请确认无重要文件

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
