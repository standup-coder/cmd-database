---
{
  "cmd_name": "bzip2",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gzip",
    "xz"
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

# bzip2

> 块排序文件压缩工具

## 用法

```
bzip2 [OPTIONS] [FILE...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 解压缩 |
| `-k` | 保留原文件 |
| `-f` | 强制覆盖 |

## 示例

### 示例 1: 压缩 file.txt

```bash
bzip2 file.txt
```

### 示例 2: 解压缩并保留压缩包

```bash
bzip2 -dk file.txt.bz2
```

## 关联命令

- [[gzip]]
- [[xz]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
