---
cmd_name: mysql_secure_installation
cmd_category: "数据库工具/MySQL工具"
cmd_dimension: Database
cmd_install: Included with MySQL Server installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Script to improve MySQL installation security"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/database/mysql.yaml
---


# mysql_secure_installation

> Script to improve MySQL installation security

## 安装

```bash
Included with MySQL Server installation
```

## 用法

```
mysql_secure_installation
```

## 示例

### 示例 1: Run interactive security configuration wizard

```bash
mysql_secure_installation
```

## 风险提示

> ⚠️ **MEDIUM**: Changes security settings; may lock out users if misconfigured

## 所属维度

[[Redis工具-MOC|Database]]
