---
{
  "cmd_name": "tmux",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "包管理器安装，如 sudo apt install tmux / sudo yum install tmux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "screen",
    "nohup"
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

# tmux

> 终端复用器，支持会话持久化和多窗口

## 安装

```bash
包管理器安装，如 sudo apt install tmux / sudo yum install tmux
```

## 用法

```
tmux [OPTIONS] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `new -s` | 创建命名会话 |
| `attach -t` | 重新附加到会话 |
| `ls` | 列出所有会话 |

## 示例

### 示例 1: 创建名为 mysession 的会话

```bash
tmux new -s mysession
```

### 示例 2: 重新连接到 mysession

```bash
tmux attach -t mysession
```

## 风险提示

> ⚠️ **LOW**: 注意在 tmux 中启动的后台进程会在会话退出后继续运行

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
