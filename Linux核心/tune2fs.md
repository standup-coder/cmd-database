---
{
  "cmd_name": "tune2fs",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mkfs",
    "fsck"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# tune2fs

> 调整 ext2/3/4 文件系统参数

## 用法

```
tune2fs [OPTIONS] DEVICE
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出超级块信息 |
| `-L` | 设置卷标 |
| `-m` | 保留块百分比 |

## 示例

### 示例 1: 查看文件系统信息

```bash
sudo tune2fs -l /dev/sda1
```

### 示例 2: 设置卷标

```bash
sudo tune2fs -L rootfs /dev/sda1
```

## 关联命令

- [[mkfs]]
- [[fsck]]

## 风险提示

> ⚠️ **HIGH**: tune2fs 修改文件系统元数据，请确认参数并备份

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
