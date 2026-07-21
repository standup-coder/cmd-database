---
{
  "cmd_name": "anacron",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "crontab",
    "at"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# anacron

> 用于非 24x7 机器执行周期性任务

## 用法

```
anacron [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 立即执行 |
| `-n` | 忽略延迟 |
| `-T` | 测试 anacrontab |

## 示例

### 示例 1: 立即运行 anacron 任务

```bash
sudo anacron -f
```

### 示例 2: 检查配置文件语法

```bash
sudo anacron -T
```

## 关联命令

- [[crontab]]
- [[at]]

## 风险提示

> ⚠️ **MEDIUM**: anacron 任务会按系统启动时间补跑，脚本错误可能集中产生副作用

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
