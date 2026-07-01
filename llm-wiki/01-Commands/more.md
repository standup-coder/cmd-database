---
{
  "cmd_name": "more",
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
    "less",
    "cat",
    "head"
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

# more

> 分页查看文件内容（less的简化版）

## 用法

```
more [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-N` | 显示行号 |
| `+N` | 从第N行开始显示 |

## 示例

### 示例 1: 分页查看文件

```bash
more file.txt
```

### 示例 2: 管道分页查看

```bash
cat file.txt | more
```

## 关联命令

- [[less]]
- [[cat]]
- [[head]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
