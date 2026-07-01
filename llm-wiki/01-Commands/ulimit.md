---
{
  "cmd_name": "ulimit",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sysctl",
    "systemctl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# ulimit

> 显示或设置 shell 资源限制

## 用法

```
ulimit [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 显示所有限制 |
| `-n` | 文件描述符数量 |
| `-u` | 最大进程数 |

## 示例

### 示例 1: 显示当前资源限制

```bash
ulimit -a
```

### 示例 2: 设置最大打开文件数为 65536

```bash
ulimit -n 65536
```

## 关联命令

- [[sysctl]]

## 风险提示

> ⚠️ **MEDIUM**: 设置过低可能导致服务无法启动，过高可能耗尽系统资源

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
