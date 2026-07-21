---
{
  "cmd_name": "at",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "crontab",
    "batch"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# at

> 在指定时间执行一次性任务

## 用法

```
at [OPTIONS] TIME
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 从文件读取命令 |
| `-l` | 列出待执行作业 |
| `-r` | 删除作业 |

## 示例

### 示例 1: 安排凌晨 2 点重启

```bash
echo 'reboot' | at 02:00
```

### 示例 2: 1 小时后执行脚本

```bash
at -f backup.sh now + 1 hour
```

## 关联命令

- [[crontab]]

## 风险提示

> ⚠️ **HIGH**: at 任务会在未来以当前环境执行，错误命令可能造成严重后果，请验证脚本

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
