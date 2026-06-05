---
cmd_name: pg_isready
cmd_category: "数据库工具/PostgreSQL工具"
cmd_dimension: Database
cmd_install: Included with PostgreSQL
cmd_platforms:
- linux
- darwin
- windows
summary: "Check PostgreSQL server connection status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/database/postgresql.yaml
---


# pg_isready

> Check PostgreSQL server connection status

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
pg_isready [options]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | Database host |
| `-p` | Database port |
| `-U` | Database user |

## 示例

### 示例 1: Check if server is accepting connections

```bash
pg_isready
```

### 示例 2: Check specific host and port

```bash
pg_isready -h localhost -p 5432
```

## 风险提示

> ⚠️ **LOW**: Read-only check; no risks

## 所属维度

[[Redis工具-MOC|Database]]
