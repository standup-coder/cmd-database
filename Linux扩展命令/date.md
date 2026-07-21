---
{
  "cmd_name": "date",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "timedatectl",
    "cal"
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

# date

> 显示或设置系统日期时间

## 用法

```
date [OPTIONS] [+FORMAT]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 显示 UTC |
| `-d` | 显示指定时间 |
| `-s` | 设置时间（需 root） |

## 示例

### 示例 1: 显示当前日期时间

```bash
date
```

### 示例 2: 以指定格式输出日期

```bash
date +%Y-%m-%d
```

## 关联命令

- [[timedatectl]]

## 风险提示

> ⚠️ **MEDIUM**: 手动设置时间可能影响日志顺序和定时任务，建议使用 NTP

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
