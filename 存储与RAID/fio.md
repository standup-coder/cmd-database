---
{
  "cmd_name": "fio",
  "cmd_category": "硬件/存储与RAID",
  "cmd_dimension": "存储与RAID",
  "cmd_install": "包管理器安装，如 sudo apt install fio",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "bonnie++",
    "iostat"
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

# fio

> 灵活的 I/O 测试器

## 安装

```bash
包管理器安装，如 sudo apt install fio
```

## 用法

```
fio [OPTIONS] [JOB FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `--name` |  |
| `--filename` |  |
| `--rw` |  |
| `--bs` |  |
| `--size` |  |
| `--numjobs` |  |

## 示例

### 示例 1: 随机读测试

```bash
fio --name=test --filename=/tmp/test --rw=randread --bs=4k --size=1G
```

### 示例 2: 执行 job 文件

```bash
fio job.fio
```

## 关联命令

- [[bonnie++]]

## 风险提示

> ⚠️ **HIGH**: fio 会写入大量数据并占用 IO，请确认目标磁盘和文件系统

## 所属维度

[[存储与RAID-MOC|硬件/存储与RAID]]
