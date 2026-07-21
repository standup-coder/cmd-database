---
{
  "cmd_name": "smartctl",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "包管理器安装 smartmontools",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hdparm",
    "nvme"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/storage.yaml"
}
---

# smartctl

> SMART 硬盘健康检测

## 安装

```bash
包管理器安装 smartmontools
```

## 用法

```
smartctl [OPTIONS] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 全部信息 |
| `-H` | 健康状态 |
| `-t` | short\|long 自检 |
| `-l` | error 错误日志 |

## 示例

### 示例 1: 查看 sda 全部 SMART

```bash
sudo smartctl -a /dev/sda
```

### 示例 2: 快速健康检查

```bash
sudo smartctl -H /dev/sda
```

## 关联命令

- [[hdparm]]
- [[nvme]]

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
