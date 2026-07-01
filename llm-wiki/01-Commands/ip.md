---
{
  "cmd_name": "ip",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "iptables",
    "nmcli",
    "ss"
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

# ip

> Linux 网络配置与路由管理核心工具

## 用法

```
ip [OPTIONS] OBJECT {COMMAND}
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 显示统计 |
| `-4` | 仅 IPv4 |
| `-6` | 仅 IPv6 |
| `-br` | 简要输出 |

## 示例

### 示例 1: 显示网卡地址

```bash
ip addr show
```

### 示例 2: 添加默认路由

```bash
sudo ip route add default via 192.168.1.1
```

## 关联命令

- [[iptables]]
- [[nmcli]]
- [[ss]]

## 风险提示

> ⚠️ **HIGH**: 修改地址、路由或链路状态可能导致网络中断，远程操作时尤其危险

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
