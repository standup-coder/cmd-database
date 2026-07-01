---
{
  "cmd_name": "journalctl",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "systemctl",
    "dmesg"
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

# journalctl

> 查询 systemd 日志

## 用法

```
journalctl [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 指定服务单元 |
| `-f` | 实时跟踪 |
| `--since` | 指定开始时间 |
| `--no-pager` | 不分页 |

## 示例

### 示例 1: 查看 nginx 服务日志

```bash
journalctl -u nginx
```

### 示例 2: 实时跟踪 myapp 日志

```bash
journalctl -f -u myapp
```

## 关联命令

- [[dmesg]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
