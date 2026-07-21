---
{
  "cmd_name": "dropuser",
  "cmd_category": "Database",
  "cmd_dimension": "Database",
  "cmd_install": "Included with PostgreSQL",
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
  "source_file": "data/database/postgresql.yaml"
}
---

# dropuser

> Remove a PostgreSQL user

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
dropuser [options] username
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database admin user |
| `-i` | Prompt before deletion |

## 示例

### 示例 1: Drop user

```bash
dropuser myuser
```

### 示例 2: Drop user with confirmation

```bash
dropuser -i myuser
```

## 风险提示

> ⚠️ **HIGH**: Removes user access; may affect running applications

## 所属维度

[[MySQL工具-MOC|Database]]
