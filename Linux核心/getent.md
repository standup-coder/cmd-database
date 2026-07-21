---
{
  "cmd_name": "getent",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "id",
    "hostname"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# getent

> 查询系统数据库条目

## 用法

```
getent [OPTIONS] DATABASE [KEY]
```

## 参数

| Flag | Description |
|------|-------------|
| `passwd` | 用户 |
| `group` | 组 |
| `hosts` | 主机 |
| `services` | 服务 |

## 示例

### 示例 1: 查询 root 用户信息

```bash
getent passwd root
```

### 示例 2: 查询主机名解析

```bash
getent hosts example.com
```

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
