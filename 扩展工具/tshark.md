---
{
  "cmd_name": "tshark",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install tshark",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "tcpdump",
    "wireshark"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# tshark

> Wireshark 命令行抓包工具

## 安装

```bash
包管理器安装，如 sudo apt install tshark
```

## 用法

```
tshark [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 指定网卡 |
| `-w` | 写入 pcap 文件 |
| `-f` | 设置捕获过滤器 |
| `-r` | 读取 pcap |

## 示例

### 示例 1: 在 eth0 抓包并保存

```bash
sudo tshark -i eth0 -w capture.pcap
```

### 示例 2: 读取并过滤 HTTP 包

```bash
tshark -r capture.pcap -Y http
```

## 关联命令

- [[tcpdump]]

## 风险提示

> ⚠️ **HIGH**: 抓包会捕获敏感流量，请遵守数据隐私与合规要求

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
