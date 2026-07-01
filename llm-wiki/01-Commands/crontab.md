---
{
  "cmd_name": "crontab",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "systemctl",
    "at"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# crontab

> 管理用户定时任务

## 用法

```
crontab [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 列出当前用户的 crontab |
| `-e` | 编辑 crontab |
| `-r` | 删除当前用户的 crontab |

## 示例

### 示例 1: 列出当前用户定时任务

```bash
crontab -l
```

### 示例 2: 编辑定时任务

```bash
crontab -e
```

## 关联命令

- [[at]]

## 风险提示

> ⚠️ **HIGH**: 错误的定时任务可能反复执行危险命令，编辑前请备份并验证

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
