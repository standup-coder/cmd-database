---
{
  "cmd_name": "passwd",
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
    "sudo"
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

# passwd

> 修改用户密码

## 用法

```
passwd [OPTIONS] [LOGIN]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 锁定密码 |
| `-u` | 解锁密码 |
| `-d` | 删除密码 |

## 示例

### 示例 1: 修改当前用户密码

```bash
passwd
```

### 示例 2: 修改 alice 密码

```bash
sudo passwd alice
```

## 关联命令

- [[useradd]]
- [[sudo]]

## 风险提示

> ⚠️ **HIGH**: 锁定或删除密码会导致无法登录，请谨慎使用 root 权限

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
