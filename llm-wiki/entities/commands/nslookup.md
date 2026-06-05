---
cmd_name: nslookup
cmd_category: 网络工具/DNS工具
cmd_dimension: DNS工具
cmd_install: ''
cmd_platforms:
- linux
- darwin
- windows
summary: "查询DNS信息"
cmd_level: intermediate
cmd_related:
- dig
- host
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/network/dns.yaml
---


# nslookup

> 查询DNS信息

## 用法

```
nslookup [name] [server]
```

## 示例

### 示例 1: 查询域名

```bash
nslookup example.com
```

### 示例 2: 使用指定DNS服务器查询

```bash
nslookup example.com 8.8.8.8
```

## 关联命令

- [[dig]]
- [[host]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[DNS工具-MOC|网络工具/DNS工具]]
