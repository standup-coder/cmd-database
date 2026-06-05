---
cmd_name: tcpdump
cmd_category: 网络工具/网络诊断
cmd_dimension: 网络诊断
cmd_install: apt install tcpdump (Ubuntu) 或 yum install tcpdump (CentOS)
cmd_platforms:
- linux
- darwin
summary: "抓取和分析网络包"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/network/diagnostic.yaml
---


# tcpdump

> 抓取和分析网络包

## 安装

```bash
apt install tcpdump (Ubuntu) 或 yum install tcpdump (CentOS)
```

## 用法

```
tcpdump [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i <interface>` | 指定网络接口 |
| `-n` | 不解析主机名 |
| `-c <count>` | 抓取指定数量的包 |
| `-w <file>` | 写入文件 |

## 示例

### 示例 1: 抓取eth0网卡的包

```bash
tcpdump -i eth0
```

### 示例 2: 抓取80端口的包

```bash
tcpdump -i eth0 port 80
```

### 示例 3: 保存到文件

```bash
tcpdump -i eth0 -w capture.pcap
```

## 风险提示

> ⚠️ **MEDIUM**: 可能捕获敏感信息，注意数据安全

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]
