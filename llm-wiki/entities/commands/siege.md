---
cmd_name: siege
cmd_category: "网络工具/HTTP工具"
cmd_dimension: Network Tools
cmd_install: Install siege package
cmd_platforms:
- linux
- darwin
summary: "HTTP load testing and benchmarking utility"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/network/http.yaml
---


# siege

> HTTP load testing and benchmarking utility

## 安装

```bash
Install siege package
```

## 用法

```
siege [options] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Number of concurrent users |
| `-t` | Time to run test (e.g., 1M for 1 minute) |
| `-r` | Number of repetitions |

## 示例

### 示例 1: Test with 25 users for 1 minute

```bash
siege -c 25 -t 1M http://example.com
```

### 示例 2: 50 users making 100 requests each

```bash
siege -c 50 -r 100 http://example.com
```

## 风险提示

> ⚠️ **HIGH**: Load testing may overwhelm target server

## 所属维度

[[HTTP工具-MOC|Network Tools]]
