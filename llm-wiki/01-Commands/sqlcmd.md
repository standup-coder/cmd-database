---
{
  "cmd_name": "sqlcmd",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.microsoft.com/sql/tools/sqlcmd-utility",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "osql",
    "tsql"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# sqlcmd

> SQL Server 命令行工具

## 安装

```bash
参考 https://docs.microsoft.com/sql/tools/sqlcmd-utility
```

## 用法

```
sqlcmd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | 服务器 |
| `-d` | 数据库 |
| `-U` | 用户 |
| `-Q` | 查询 |
| `-i` | 输入文件 |

## 示例

### 示例 1: 执行查询

```bash
sqlcmd -S localhost -d mydb -U sa -Q 'SELECT @@VERSION'
```

### 示例 2: 执行脚本并输出

```bash
sqlcmd -S localhost -i script.sql -o output.txt
```

## 风险提示

> ⚠️ **MEDIUM**: sqlcmd 可直接执行 DDL/DML，生产环境请确认脚本内容

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
