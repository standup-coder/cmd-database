---
{
  "cmd_name": "whatis",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "man",
    "apropos"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# whatis

> 显示命令简短描述

## 用法

```
whatis [OPTIONS] KEYWORD
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 正则匹配 |
| `-w` | 精确匹配 |

## 示例

### 示例 1: 显示 ls 简介

```bash
whatis ls
```

### 示例 2: 精确匹配

```bash
whatis -w passwd
```

## 关联命令

- [[man]]
- [[apropos]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
