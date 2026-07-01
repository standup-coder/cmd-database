---
{
  "cmd_name": "less",
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
    "more",
    "cat",
    "tail"
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

# less

> 分页查看文件内容，支持前后翻页

## 用法

```
less [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-N` | 显示行号 |
| `-i` | 搜索时忽略大小写 |
| `-S` | 截断长行不换行 |
| `+F` | 类似tail -f，实时跟踪文件 |

## 示例

### 示例 1: 分页查看系统日志

```bash
less /var/log/syslog
```

### 示例 2: 实时跟踪日志文件

```bash
less +F /var/log/nginx/access.log
```

## 关联命令

- [[more]]
- [[cat]]
- [[tail]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
