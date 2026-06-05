---
cmd_name: ping
cmd_category: 网络工具/网络诊断
cmd_dimension: 网络诊断
cmd_install: ''
cmd_platforms:
- linux
- darwin
- windows
summary: "测试网络连通性"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/network/diagnostic.yaml
---


# ping

> 测试网络连通性

## 用法

```
ping [options] <host>
```

## 参数

| Flag | Description |
|------|-------------|
| `-c <count>` | 发送指定数量的包 |
| `-i <interval>` | 发送间隔(秒) |
| `-t <ttl>` | 设置TTL值 |

## 示例

### 示例 1: ping域名

```bash
ping google.com
```

### 示例 2: 发送4个包

```bash
ping -c 4 192.168.1.1
```

## 所属维度

[[网络诊断-MOC|网络工具/网络诊断]]
