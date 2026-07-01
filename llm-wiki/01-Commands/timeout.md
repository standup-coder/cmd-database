---
{
  "cmd_name": "timeout",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nohup",
    "cron"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# timeout

> 在指定时间后终止命令

## 用法

```
timeout [OPTIONS] DURATION COMMAND [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 指定发送的信号 |
| `-k` | 强制终止前的宽限时间 |
| `--preserve-status` | 保留退出码 |

## 示例

### 示例 1: 30 秒后终止 job.sh

```bash
timeout 30s ./job.sh
```

### 示例 2: 10 分钟后强制 kill

```bash
timeout -s 9 10m ./long-task
```

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
