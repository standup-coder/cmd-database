---
cmd_name: redis-cli INFO
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Included with Redis installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Get Redis server information and statistics"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-cli INFO

> Get Redis server information and statistics

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-cli INFO [section]
```

## 示例

### 示例 1: Get all server information

```bash
redis-cli INFO
```

### 示例 2: Get server section info

```bash
redis-cli INFO server
```

### 示例 3: Get memory usage statistics

```bash
redis-cli INFO memory
```

### 示例 4: Get replication information

```bash
redis-cli INFO replication
```

### 示例 5: Get general statistics

```bash
redis-cli INFO stats
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; no risks

## 所属维度

[[Redis工具-MOC|Database]]
