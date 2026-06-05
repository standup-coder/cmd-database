---
cmd_name: redis-check-rdb
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Included with Redis installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Check Redis RDB snapshot file"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-check-rdb

> Check Redis RDB snapshot file

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-check-rdb <dump.rdb>
```

## 示例

### 示例 1: Check RDB file integrity

```bash
redis-check-rdb dump.rdb
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; safe to use

## 所属维度

[[Redis工具-MOC|Database]]
