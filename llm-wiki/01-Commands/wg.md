---
{
  "cmd_name": "wg",
  "cmd_category": "网络工具/基础设施",
  "cmd_dimension": "基础设施",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "openvpn",
    "ip"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/infra.yaml"
}
---

# wg

> WireGuard 快速、现代、安全的 VPN

## 用法

```
wg [OPTIONS] [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `show` | 显示接口 |
| `set` | 设置接口 |
| `genkey` | 生成私钥 |
| `pubkey` | 生成公钥 |

## 示例

### 示例 1: 生成密钥对

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

### 示例 2: 显示 WireGuard 接口

```bash
sudo wg show
```

## 关联命令

- [[openvpn]]
- [[ip]]

## 风险提示

> ⚠️ **MEDIUM**: 私钥泄露会导致 VPN 被攻破，请安全存储

## 所属维度

[[基础设施-MOC|网络工具/基础设施]]
