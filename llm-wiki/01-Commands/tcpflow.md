---
{
  "cmd_name": "tcpflow",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install tcpflow",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "tcpdump",
    "tshark"
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

# tcpflow

> TCP 流重组与捕获工具

## 安装

```bash
包管理器安装，如 sudo apt install tcpflow
```

## 用法

```
tcpflow [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 指定网卡 |
| `-o` | 输出目录 |
| `-c` | 输出到控制台 |

## 示例

### 示例 1: 捕获 eth0 上 80 端口的 TCP 流

```bash
sudo tcpflow -i eth0 port 80
```

### 示例 2: 从 pcap 重组流

```bash
tcpflow -r capture.pcap
```

## 关联命令

- [[tcpdump]]
- [[tshark]]

## 风险提示

> ⚠️ **HIGH**: 重组流会还原明文数据，请遵守隐私政策

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
