---
{
  "cmd_name": "rethinkdb",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://rethinkdb.com/docs/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "mongo",
    "redis"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# rethinkdb

> RethinkDB 分布式文档数据库

## 安装

```bash
参考 https://rethinkdb.com/docs/install/
```

## 用法

```
rethinkdb [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--bind` | all |
| `--join` | 加入集群 |
| `--directory` | 数据目录 |

## 示例

### 示例 1: 监听所有接口启动

```bash
rethinkdb --bind all
```

### 示例 2: 加入集群

```bash
rethinkdb --join host:29015 --directory ./data
```

## 关联命令

- [[redis]]

## 风险提示

> ⚠️ **MEDIUM**: 默认无认证，请勿直接暴露公网

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
