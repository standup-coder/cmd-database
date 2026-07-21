---
{
  "cmd_name": "timedatectl",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "date",
    "hwclock"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# timedatectl

> 查看和设置系统时间与日期

## 用法

```
timedatectl [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `status` | 显示当前时间状态 |
| `set-time` | 设置系统时间 |
| `set-timezone` | 设置时区 |

## 示例

### 示例 1: 查看当前时区和时间状态

```bash
timedatectl status
```

### 示例 2: 设置系统时区为上海

```bash
sudo timedatectl set-timezone Asia/Shanghai
```

## 关联命令

- [[date]]

## 风险提示

> ⚠️ **MEDIUM**: 修改时间可能影响日志顺序和定时任务，请谨慎操作

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
