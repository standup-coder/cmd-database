---
{
  "cmd_name": "touch",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mkdir",
    "ls"
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

# touch

> 更新文件时间戳或创建空文件

## 用法

```
touch [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 只更新访问时间 |
| `-m` | 只更新修改时间 |
| `-c` | 不创建新文件 |

## 示例

### 示例 1: 创建或更新 file.txt 时间戳

```bash
touch file.txt
```

### 示例 2: 设置指定时间

```bash
touch -t 202401011200 file.txt
```

## 关联命令

- [[mkdir]]
- [[ls]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
