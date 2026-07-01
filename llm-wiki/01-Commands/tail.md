---
{
  "cmd_name": "tail",
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
    "head",
    "less",
    "watch"
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

# tail

> 显示文件末尾部分，支持实时跟踪

## 用法

```
tail [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n <N>` | 显示最后N行（默认10行） |
| `-f` | 实时跟踪文件追加内容 |
| `-F` | 跟踪并处理日志轮转 |

## 示例

### 示例 1: 实时跟踪系统日志

```bash
tail -f /var/log/syslog
```

### 示例 2: 显示文件最后50行

```bash
tail -n 50 file.txt
```

## 关联命令

- [[head]]
- [[less]]
- [[watch]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
