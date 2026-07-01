---
{
  "cmd_name": "kill",
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
    "ps",
    "top",
    "killall"
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

# kill

> 向进程发送信号以终止或控制

## 用法

```
kill [信号] PID...
```

## 参数

| Flag | Description |
|------|-------------|
| `-9` | SIGKILL，强制终止（不可捕获） |
| `-15` | SIGTERM，优雅终止（默认） |
| `-l` | 列出所有信号名称 |

## 示例

### 示例 1: 优雅终止PID 1234

```bash
kill 1234
```

### 示例 2: 强制终止PID 1234

```bash
kill -9 1234
```

### 示例 3: 列出所有可用信号

```bash
kill -l
```

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
