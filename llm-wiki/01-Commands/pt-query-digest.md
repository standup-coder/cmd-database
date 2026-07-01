---
{
  "cmd_name": "pt-query-digest",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.percona.com/percona-toolkit/installation.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mysql",
    "mysqldumpslow"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# pt-query-digest

> Percona Toolkit 慢查询分析工具

## 安装

```bash
参考 https://docs.percona.com/percona-toolkit/installation.html
```

## 用法

```
pt-query-digest [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--filter` | 过滤 |
| `--limit` | 限制输出 |
| `--output` | 输出格式 |

## 示例

### 示例 1: 分析慢查询日志

```bash
pt-query-digest /var/log/mysql/slow.log
```

### 示例 2: 只显示 Top 10

```bash
pt-query-digest --limit 10 slow.log
```

## 关联命令

- [[mysql]]

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
