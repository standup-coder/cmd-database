---
{
  "cmd_name": "sh",
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
    "bash",
    "zsh",
    "chmod"
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

# sh

> Bourne Shell，标准的Unix命令解释器

## 用法

```
sh [选项] [脚本文件] [参数...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 执行命令字符串 |
| `-x` | 打印执行的每条命令 |
| `-e` | 命令失败时立即退出 |

## 示例

### 示例 1: 执行命令字符串

```bash
sh -c 'echo hello'
```

### 示例 2: 执行shell脚本并传递参数

```bash
sh script.sh arg1 arg2
```

## 关联命令

- [[bash]]
- [[zsh]]
- [[chmod]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
