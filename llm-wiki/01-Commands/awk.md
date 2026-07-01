---
{
  "cmd_name": "awk",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "unix"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sed",
    "grep",
    "cut"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# awk

> 文本处理语言，按模式扫描和处理文件

## 用法

```
awk 'pattern { action }' [file...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-F` | 指定字段分隔符 |
| `-v` | 赋值变量 |
| `-f` | 从文件读取awk脚本 |

## 示例

### 示例 1: 打印每行第一个字段

```bash
awk '{print $1}' file.txt
```

### 示例 2: 以冒号分隔打印第一个字段

```bash
awk -F: '{print $1}' /etc/passwd
```

### 示例 3: 匹配pattern的行

```bash
awk '/pattern/ {print $0}' file.txt
```

## 关联命令

- [[sed]]
- [[grep]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
