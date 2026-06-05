---
cmd_name: dig
cmd_category: 网络工具/DNS工具
cmd_dimension: DNS工具
cmd_install: apt install dnsutils (Ubuntu) 或 yum install bind-utils (CentOS)
cmd_platforms:
- linux
- darwin
- unix
summary: "DNS查询工具"
cmd_level: intermediate
cmd_related:
- nslookup
- host
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/network/dns.yaml
---


# dig

> DNS查询工具

## 安装

```bash
apt install dnsutils (Ubuntu) 或 yum install bind-utils (CentOS)
```

## 用法

```
dig [@server] name [type]
```

## 参数

| Flag | Description |
|------|-------------|
| `+short` | 简洁输出 |
| `+trace` | 跟踪DNS解析过程 |
| `-x <ip>` | 反向DNS查询 |
| `@<server>` | 指定DNS服务器 |

## 示例

### 示例 1: 查询域名A记录

```bash
dig example.com
```

### 示例 2: 查询MX记录

```bash
dig example.com MX
```

### 示例 3: 使用指定DNS服务器简洁查询

```bash
dig @8.8.8.8 example.com +short
```

### 示例 4: 反向DNS查询

```bash
dig -x 8.8.8.8
```

## 关联命令

- [[nslookup]]
- [[host]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 参考链接

- [https://linux.die.net/man/1/dig](https://linux.die.net/man/1/dig)

## 所属维度

[[DNS工具-MOC|网络工具/DNS工具]]
