---
{
  "cmd_name": "iwconfig",
  "cmd_category": "硬件/网络硬件",
  "cmd_dimension": "网络硬件",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "iw",
    "nmcli"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/network.yaml"
}
---

# iwconfig

> 传统无线接口配置

## 用法

```
iwconfig [INTERFACE] [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `essid` | 设置 SSID |
| `mode` | 模式 |
| `key` | 密钥 |
| `ap` | 接入点 |

## 示例

### 示例 1: 查看无线配置

```bash
iwconfig
```

### 示例 2: 连接 WiFi

```bash
sudo iwconfig wlan0 essid MyWiFi key s:mypassword
```

## 关联命令

- [[iw]]
- [[nmcli]]

## 风险提示

> ⚠️ **MEDIUM**: 命令行输入 WiFi 密钥会留在历史记录

## 所属维度

[[网络硬件-MOC|硬件/网络硬件]]
