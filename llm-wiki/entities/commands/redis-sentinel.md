---
cmd_name: redis-sentinel
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Included with Redis installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Redis Sentinel for high availability"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-sentinel

> Redis Sentinel for high availability

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-sentinel [config_file]
```

## 示例

### 示例 1: Start Redis Sentinel with config

```bash
redis-sentinel /etc/redis/sentinel.conf
```

### 示例 2: Start in Sentinel mode

```bash
redis-sentinel sentinel.conf --sentinel
```

## 风险提示

> ⚠️ **HIGH**: Manages automatic failover; misconfiguration can cause data loss

## 所属维度

[[Redis工具-MOC|Database]]
