---
cmd_name: host
cmd_category: 网络工具/DNS工具
cmd_dimension: DNS工具
cmd_install: apt install bind9-host (Ubuntu)
cmd_platforms:
- linux
- darwin
- unix
summary: "简单的DNS查询工具"
cmd_level: beginner
cmd_related:
- dig
- nslookup
cmd_tags:
- beginner
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/network/dns.yaml
---


# host

> 简单的DNS查询工具

## 安装

```bash
apt install bind9-host (Ubuntu)
```

## 用法

```
host [options] name [server]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t <type>` | 指定查询类型 |
| `-a` | 详细查询 |

## 示例

### 示例 1: 查询域名

```bash
host example.com
```

### 示例 2: 查询MX记录

```bash
host -t MX example.com
```

## 关联命令

- [[dig]]
- [[nslookup]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[DNS工具-MOC|网络工具/DNS工具]]
