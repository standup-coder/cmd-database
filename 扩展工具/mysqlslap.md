---
{
  "cmd_name": "mysqlslap",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 MySQL 客户端安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mysql",
    "mysqladmin"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# mysqlslap

> MySQL 负载模拟与压测工具

## 安装

```bash
随 MySQL 客户端安装
```

## 用法

```
mysqlslap [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--auto-generate-sql` |  |
| `--concurrency` |  |
| `--iterations` |  |
| `--engine` |  |

## 示例

### 示例 1: 自动生成 SQL 压测

```bash
mysqlslap --auto-generate-sql --concurrency=10 --iterations=100
```

### 示例 2: 压测指定查询

```bash
mysqlslap --query='SELECT 1' --concurrency=50
```

## 关联命令

- [[mysql]]
- [[mysqladmin]]

## 风险提示

> ⚠️ **HIGH**: 压测会影响生产库性能，请在测试环境或低峰期执行

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
