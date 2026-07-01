---
{
  "cmd_name": "termshark",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "pip install termshark 或参考 https://github.com/gcla/termshark",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "tshark",
    "tcpdump"
  ],
  "cmd_tags": [
    "advanced",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# termshark

> 终端交互式 TUI 抓包工具

## 安装

```bash
pip install termshark 或参考 https://github.com/gcla/termshark
```

## 用法

```
termshark [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 指定网卡 |
| `-r` | 读取 pcap |
| `-f` | 捕获过滤器 |

## 示例

### 示例 1: 终端交互式抓包

```bash
sudo termshark -i eth0
```

### 示例 2: 交互式查看 pcap

```bash
termshark -r capture.pcap
```

## 关联命令

- [[tshark]]
- [[tcpdump]]

## 风险提示

> ⚠️ **HIGH**: 查看网络流量可能涉及敏感信息，请确保授权

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
