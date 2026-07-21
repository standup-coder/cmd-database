---
{
  "cmd_name": "sysctl",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "systemctl",
    "dmesg"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# sysctl

> 运行时内核参数管理

## 用法

```
sysctl [OPTIONS] [VARIABLE[=VALUE]...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 列出所有参数 |
| `-w` | 临时写入 |
| `-p` | 从文件加载 |
| `-n` | 只输出值 |

## 示例

### 示例 1: 查看 IP 转发设置

```bash
sysctl -a | grep ipv4.ip_forward
```

### 示例 2: 临时开启 IP 转发

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

## 关联命令

- [[dmesg]]

## 风险提示

> ⚠️ **HIGH**: 错误的内核参数可能导致系统不稳定或网络异常，修改前请了解含义

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
