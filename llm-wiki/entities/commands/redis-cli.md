---
cmd_name: redis-cli
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Install Redis package or build from source
cmd_platforms:
- linux
- darwin
- windows
summary: "Redis command-line interface client"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-cli

> Redis command-line interface client

## 安装

```bash
Install Redis package or build from source
```

## 用法

```
redis-cli [options] [command]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | Server hostname (default: 127.0.0.1) |
| `-p` | Server port (default: 6379) |
| `-a` | Password for authentication |
| `-n` | Database number |
| `--scan` | Scan keys using pattern |
| `--bigkeys` | Find big keys in database |
| `--latency` | Monitor latency |

## 示例

### 示例 1: Connect to local Redis server

```bash
redis-cli
```

### 示例 2: Connect to remote Redis server

```bash
redis-cli -h 192.168.1.100 -p 6379
```

### 示例 3: Connect with password authentication

```bash
redis-cli -a mypassword
```

### 示例 4: Execute single command

```bash
redis-cli PING
```

### 示例 5: Scan keys matching pattern

```bash
redis-cli --scan --pattern 'user:*'
```

### 示例 6: Find largest keys in database

```bash
redis-cli --bigkeys
```

## 风险提示

> ⚠️ **HIGH**: Direct database access; can modify or delete data

## 所属维度

[[Redis工具-MOC|Database]]
