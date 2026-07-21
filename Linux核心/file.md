---
{
  "cmd_name": "file",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "xxd",
    "ls"
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

# file

> 识别文件类型

## 用法

```
file [OPTIONS] FILE
```

## 参数

| Flag | Description |
|------|-------------|
| `-b` | 不显示文件名 |
| `-i` | 显示 MIME 类型 |
| `-L` | 跟随符号链接 |

## 示例

### 示例 1: 识别文件类型

```bash
file /bin/ls
```

### 示例 2: 显示 MIME 类型

```bash
file -i image.png
```

## 关联命令

- [[xxd]]
- [[ls]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
