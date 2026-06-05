---
cmd_name: redis-cli SAVE
cmd_category: "数据库工具/Redis工具"
cmd_dimension: Database
cmd_install: Included with Redis installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Synchronously save dataset to disk"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/database/redis.yaml
---


# redis-cli SAVE

> Synchronously save dataset to disk

## 安装

```bash
Included with Redis installation
```

## 用法

```
redis-cli SAVE
```

## 示例

### 示例 1: Force synchronous save

```bash
redis-cli SAVE
```

### 示例 2: Background save (non-blocking)

```bash
redis-cli BGSAVE
```

## 风险提示

> ⚠️ **HIGH**: SAVE blocks server until complete; use BGSAVE for production

## 所属维度

[[Redis工具-MOC|Database]]
