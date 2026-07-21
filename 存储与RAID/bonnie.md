---
{
  "cmd_name": "bonnie++",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "包管理器安装，如 sudo apt install bonnie++",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "fio",
    "hdparm"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/hardware/storage.yaml"
}
---

# bonnie++

> 文件系统性能基准测试

## 安装

```bash
包管理器安装，如 sudo apt install bonnie++
```

## 用法

```
bonnie++ [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 测试目录 |
| `-u` | 用户 |
| `-r` | 内存大小 |
| `-s` | 文件大小 |

## 示例

### 示例 1: 测试 /tmp

```bash
bonnie++ -d /tmp -u root
```

### 示例 2: 简化测试

```bash
bonnie++ -f -n 0 -r 4096 -d /mnt
```

## 关联命令

- [[fio]]
- [[hdparm]]

## 风险提示

> ⚠️ **HIGH**: 会创建大文件并大量读写，请确认目录空间和权限

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
