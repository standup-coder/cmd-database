---
{
  "cmd_name": "head",
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
    "tail",
    "cat",
    "less"
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

# head

> 显示文件开头部分

## 用法

```
head [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n <N>` | 显示前N行（默认10行） |
| `-c <N>` | 显示前N字节 |
| `-q` | 不显示文件名标题 |

## 示例

### 示例 1: 显示文件前20行

```bash
head -n 20 file.txt
```

### 示例 2: 显示文件前100字节

```bash
head -c 100 file.bin
```

## 关联命令

- [[tail]]
- [[cat]]
- [[less]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
