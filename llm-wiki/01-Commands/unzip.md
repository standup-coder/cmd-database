---
{
  "cmd_name": "unzip",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "zip",
    "tar"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# unzip

> 解压 ZIP 归档

## 用法

```
unzip [OPTIONS] ARCHIVE
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 指定解压目录 |
| `-o` | 覆盖现有文件 |
| `-l` | 列出内容 |

## 示例

### 示例 1: 解压到指定目录

```bash
unzip archive.zip -d /tmp/extract
```

### 示例 2: 列出归档内容

```bash
unzip -l archive.zip
```

## 关联命令

- [[zip]]
- [[tar]]

## 风险提示

> ⚠️ **MEDIUM**: -o 会直接覆盖目标文件，建议先查看内容

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
