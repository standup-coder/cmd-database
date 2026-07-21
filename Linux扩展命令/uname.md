---
{
  "cmd_name": "uname",
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
    "cat /etc/os-release"
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

# uname

> 显示系统内核信息

## 用法

```
uname [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有信息 |
| `-r` | 显示内核版本 |
| `-m` | 显示机器硬件名 |

## 示例

### 示例 1: 显示完整系统信息

```bash
uname -a
```

### 示例 2: 显示内核版本

```bash
uname -r
```

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
