---
{
  "cmd_name": "htop",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "包管理器安装，如 sudo apt install htop / sudo yum install htop",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "top",
    "ps"
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

# htop

> 交互式进程查看器

## 安装

```bash
包管理器安装，如 sudo apt install htop / sudo yum install htop
```

## 用法

```
htop [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 只显示指定用户的进程 |
| `-p` | 只显示指定 PID |

## 示例

### 示例 1: 启动交互式进程浏览器

```bash
htop
```

### 示例 2: 只查看 nginx 用户的进程

```bash
htop -u nginx
```

## 风险提示

> ⚠️ **LOW**: 只读命令，但注意 kill 快捷键会发送信号

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
