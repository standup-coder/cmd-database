---
cmd_name: ab
cmd_category: "网络工具/HTTP工具"
cmd_dimension: Network Tools
cmd_install: Install apache2-utils (Linux) or httpd (Mac)
cmd_platforms:
- linux
- darwin
- windows
summary: "Apache HTTP server benchmarking tool"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/network/http.yaml
---


# ab

> Apache HTTP server benchmarking tool

## 安装

```bash
Install apache2-utils (Linux) or httpd (Mac)
```

## 用法

```
ab [options] URL
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Number of requests |
| `-c` | Number of concurrent requests |
| `-t` | Maximum time for benchmarking |
| `-k` | Enable HTTP KeepAlive |

## 示例

### 示例 1: Send 1000 requests with 10 concurrent

```bash
ab -n 1000 -c 10 http://example.com/
```

### 示例 2: Benchmark for 30 seconds with 50 concurrent

```bash
ab -t 30 -c 50 http://example.com/
```

## 风险提示

> ⚠️ **HIGH**: High load testing may overwhelm target server

## 所属维度

[[HTTP工具-MOC|Network Tools]]
