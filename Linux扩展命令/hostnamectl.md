---
{
  "cmd_name": "hostnamectl",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hostname",
    "timedatectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# hostnamectl

> 查看和设置主机名

## 用法

```
hostnamectl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `status` | 查看状态 |
| `set-hostname` | 设置静态主机名 |
| `set-icon-name` | 设置图标名 |

## 示例

### 示例 1: 查看主机名信息

```bash
hostnamectl status
```

### 示例 2: 设置主机名为 web01

```bash
sudo hostnamectl set-hostname web01
```

## 关联命令

- [[timedatectl]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
