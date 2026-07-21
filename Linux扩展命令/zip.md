---
{
  "cmd_name": "zip",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "unzip",
    "tar"
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

# zip

> 创建 ZIP 归档

## 用法

```
zip [OPTIONS] ARCHIVE FILES...
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 递归压缩目录 |
| `-e` | 加密 |
| `-q` | 静默模式 |

## 示例

### 示例 1: 递归压缩 docs 目录

```bash
zip -r backup.zip docs/
```

### 示例 2: 创建加密 ZIP

```bash
zip -e secret.zip file.txt
```

## 关联命令

- [[unzip]]
- [[tar]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
