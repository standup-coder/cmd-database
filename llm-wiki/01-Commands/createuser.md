---
{
  "cmd_name": "createuser",
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

# createuser

> Create a new PostgreSQL user

## 安装

```bash
Included with PostgreSQL
```

## 用法

```
createuser [options] username
```

## 参数

| Flag | Description |
|------|-------------|
| `-U` | Database admin user |
| `-s` | Create superuser |
| `-d` | User can create databases |
| `-P` | Prompt for password |

## 示例

### 示例 1: Create user with password

```bash
createuser -P myuser
```

### 示例 2: Create superuser with password

```bash
createuser -s -P admin
```

### 示例 3: Create user who can create databases

```bash
createuser -d developer
```

## 风险提示

> ⚠️ **HIGH**: Creating superuser grants full database control

## 所属维度

[[Database-MOC|Database]]
