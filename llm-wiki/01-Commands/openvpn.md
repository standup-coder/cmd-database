---
{
  "cmd_name": "openvpn",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "wg",
    "ipsec"
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

# openvpn

> SSL/TLS VPN 解决方案

## 用法

```
openvpn [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | 配置文件 |
| `--daemon` | 后台运行 |
| `--client` | 客户端模式 |

## 示例

### 示例 1: 使用配置文件连接 VPN

```bash
sudo openvpn --config client.ovpn
```

### 示例 2: 后台启动服务端

```bash
sudo openvpn --daemon --config server.conf
```

## 关联命令

- [[wg]]

## 风险提示

> ⚠️ **MEDIUM**: VPN 配置错误会将流量导向错误网络，请确认路由和证书

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
