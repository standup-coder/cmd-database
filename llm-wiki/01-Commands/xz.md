---
{
  "cmd_name": "xz",
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
    "bzip2"
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

# xz

> 高压缩比文件压缩工具

## 用法

```
xz [OPTIONS] [FILE...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 解压缩 |
| `-k` | 保留原文件 |
| `-T` | 指定线程数 |

## 示例

### 示例 1: 压缩 file.txt

```bash
xz file.txt
```

### 示例 2: 解压缩并保留压缩包

```bash
xz -dk file.txt.xz
```

## 关联命令

- [[gzip]]
- [[bzip2]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
