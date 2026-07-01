---
{
  "cmd_name": "ifconfig",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ip",
    "route"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# ifconfig

> 传统网络接口配置工具

## 用法

```
ifconfig [INTERFACE] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `up` | 启用 |
| `down` | 禁用 |
| `inet` | 设置 IP |
| `netmask` | 设置掩码 |

## 示例

### 示例 1: 显示接口信息

```bash
ifconfig
```

### 示例 2: 配置 IP

```bash
sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0
```

## 关联命令

- [[ip]]
- [[route]]

## 风险提示

> ⚠️ **MEDIUM**: 修改 IP 或关闭接口会中断网络，远程操作时请谨慎

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
