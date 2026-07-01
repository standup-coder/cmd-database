---
{
  "cmd_name": "redis-server",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Install Redis package or build from source",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/redis.yaml"
}
---

# redis-server

> Redis server daemon

## 安装

```bash
Install Redis package or build from source
```

## 用法

```
redis-server [config_file] [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `--port` | Specify port number |
| `--bind` | Bind to specific network interface |
| `--protected-mode` | Enable/disable protected mode |
| `--daemonize` | Run as daemon |
| `--save` | Configure save points (seconds keys) |

## 示例

### 示例 1: Start Redis with default configuration

```bash
redis-server
```

### 示例 2: Start Redis with config file

```bash
redis-server /etc/redis/redis.conf
```

### 示例 3: Start on custom port

```bash
redis-server --port 6380
```

### 示例 4: Start with security settings

```bash
redis-server --bind 127.0.0.1 --protected-mode yes
```

## 风险提示

> ⚠️ **HIGH**: Running without authentication exposes data to network

## 所属维度

[[Database-MOC|Database]]
