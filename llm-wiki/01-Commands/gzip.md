---
{
  "cmd_name": "gzip",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "tar",
    "gunzip",
    "zip"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# gzip

> GNU 文件压缩工具

## 用法

```
gzip [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 解压缩 |
| `-k` | 保留原始文件 |
| `-r` | 递归处理目录 |

## 示例

### 示例 1: 压缩 file.txt 为 file.txt.gz

```bash
gzip file.txt
```

### 示例 2: 解压缩并保留压缩包

```bash
gzip -dk file.txt.gz
```

## 关联命令

- [[tar]]
- [[zip]]

## 风险提示

> ⚠️ **MEDIUM**: 默认会删除原文件，建议使用 -k 保留备份

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
