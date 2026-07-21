---
{
  "cmd_name": "bash",
  "cmd_category": "Shell脚本/Bash工具",
  "cmd_dimension": "Bash工具",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sh",
    "zsh"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/shell/bash.yaml"
}
---

# bash

> Bash Shell 解释器，执行脚本文件或交互式命令

## 用法

```
bash [选项] [脚本文件]
```

```
bash -c '命令字符串'
```

## 参数

| Flag | Description |
|------|-------------|
| `-x` | 调试模式，打印执行的每条命令 |
| `-e` | 命令出错时立即退出 |
| `-u` | 使用未定义变量时报错 |
| `-n` | 语法检查，不执行 |
| `-v` | 打印输入行 |

## 示例

### 示例 1: 调试模式执行脚本

```bash
bash -x script.sh
```

### 示例 2: 严格模式执行脚本

```bash
bash -e -u script.sh
```

### 示例 3: 仅检查语法错误

```bash
bash -n script.sh
```

### 示例 4: 执行单行命令

```bash
bash -c 'echo hello'
```

## 关联命令

- [[sh]]
- [[zsh]]

## 所属维度

[[Bash工具-MOC|Shell脚本/Bash工具]]
