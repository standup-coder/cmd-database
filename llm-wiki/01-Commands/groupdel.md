---
{
  "cmd_name": "groupdel",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groupadd",
    "gpasswd"
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

# groupdel

> 删除用户组

## 用法

```
groupdel [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--help` | 显示帮助信息 |
| `--version` | 显示版本信息 |

## 示例

### 示例 1: 删除 developers 组

```bash
sudo groupdel developers
```

### 示例 2: 确认组内是否还有成员后再删除

```bash
getent group developers
```

## 关联命令

- [[groupadd]]

## 风险提示

> ⚠️ **MEDIUM**: 删除仍有成员用户的组可能导致权限问题

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
