---
{
  "cmd_name": "dmesg",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "journalctl",
    "sysctl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# dmesg

> 查看内核环形缓冲区消息

## 用法

```
dmesg [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-T` | 人类可读时间 |
| `-l` | 按级别过滤 |
| `-w` | 实时跟踪 |
| `-n` | 设置日志级别 |

## 示例

### 示例 1: 查看带时间戳的内核日志

```bash
dmesg -T
```

### 示例 2: 实时跟踪内核日志

```bash
dmesg -w
```

## 关联命令

- [[journalctl]]
- [[sysctl]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
