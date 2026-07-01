---
{
  "cmd_name": "fgrep",
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
    "grep",
    "egrep",
    "awk"
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

# fgrep

> 固定字符串grep（等同于grep -F），禁用正则表达式

## 用法

```
fgrep [选项] 字符串 [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-x` | 整行匹配 |
| `-f` | 从文件读取匹配模式 |

## 示例

### 示例 1: 按字面匹配a*b（不解释正则）

```bash
fgrep 'a*b' file.txt
```

### 示例 2: 从文件读取多个匹配字符串

```bash
fgrep -f patterns.txt log.txt
```

## 关联命令

- [[grep]]
- [[egrep]]
- [[awk]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
