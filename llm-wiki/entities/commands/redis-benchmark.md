---
cmd_name: redis-benchmark
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Included with Redis installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Redis performance benchmarking tool"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-benchmark

> Redis performance benchmarking tool

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-benchmark [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | Server hostname |
| `-p` | Server port |
| `-c` | Number of parallel connections |
| `-n` | Total number of requests |
| `-t` | Only run specified tests (e.g., get,set) |
| `-q` | Quiet mode, show only requests per second |

## 示例

### 示例 1: Run default benchmark suite

```bash
redis-benchmark
```

### 示例 2: Quick benchmark with minimal output

```bash
redis-benchmark -q
```

### 示例 3: Benchmark GET/SET with custom parameters

```bash
redis-benchmark -t get,set -n 100000 -c 50
```

### 示例 4: Benchmark remote server

```bash
redis-benchmark -h 192.168.1.100 -p 6379
```

## 风险提示

> ⚠️ **MEDIUM**: May impact server performance during benchmark

## 所属维度

[[Redis工具-MOC|Database]]
