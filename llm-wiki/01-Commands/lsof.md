---
{
  "cmd_name": "lsof",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ps",
    "ss"
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

# lsof

> 列出已打开的文件及对应进程

## 用法

```
lsof [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 列出网络文件 |
| `-p` | 按 PID 过滤 |
| `+d` | 列出打开某目录下文件的进程 |

## 示例

### 示例 1: 查看占用 8080 端口的进程

```bash
lsof -i :8080
```

### 示例 2: 查看打开 /var/log 的进程

```bash
lsof +d /var/log
```

## 关联命令

- [[ss]]

## 风险提示

> ⚠️ **LOW**: 通常只读，某些系统可能需要 root 才能查看全部进程

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
