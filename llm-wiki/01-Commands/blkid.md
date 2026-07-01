---
{
  "cmd_name": "blkid",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lsblk",
    "mount"
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

# blkid

> 显示块设备属性（UUID、文件系统类型等）

## 用法

```
blkid [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o` | 指定输出格式 |
| `-s` | 指定显示字段 |
| `-p` | 绕过缓存 |

## 示例

### 示例 1: 列出所有块设备 UUID

```bash
sudo blkid
```

### 示例 2: 查看指定分区属性

```bash
sudo blkid /dev/sda1
```

## 关联命令

- [[lsblk]]
- [[mount]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
