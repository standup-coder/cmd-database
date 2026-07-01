---
{
  "cmd_name": "nmcli",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nmtui",
    "ip",
    "netplan"
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

# nmcli

> NetworkManager 命令行工具

## 用法

```
nmcli [OPTIONS] OBJECT {COMMAND}
```

## 参数

| Flag | Description |
|------|-------------|
| `device` | status 设备状态 |
| `connection` | up 启用连接 |
| `connection` | show 查看连接 |

## 示例

### 示例 1: 查看网卡状态

```bash
nmcli device status
```

### 示例 2: 启用指定连接

```bash
nmcli connection up 'Wired connection 1'
```

## 关联命令

- [[ip]]
- [[netplan]]

## 风险提示

> ⚠️ **MEDIUM**: 关闭或切换连接会中断网络，远程操作需谨慎

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
