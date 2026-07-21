---
{
  "cmd_name": "apropos",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "whatis",
    "man"
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

# apropos

> 按关键字搜索手册页

## 用法

```
apropos [OPTIONS] KEYWORD
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 正则 |
| `-e` | 精确匹配 |
| `-s` | 指定节 |

## 示例

### 示例 1: 搜索网络相关命令

```bash
apropos network
```

### 示例 2: 在第 1 节搜索 copy

```bash
apropos -s 1 copy
```

## 关联命令

- [[whatis]]
- [[man]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
