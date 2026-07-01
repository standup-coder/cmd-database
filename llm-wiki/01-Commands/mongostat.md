---
{
  "cmd_name": "mongostat",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongotop",
    "mongosh"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# mongostat

> 实时显示 MongoDB 实例统计信息

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongostat [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--host` | 主机 |
| `--rowcount` | 行数 |
| `--discover` | 发现副本集成员 |

## 示例

### 示例 1: 实时监控本地实例

```bash
mongostat --host localhost:27017
```

### 示例 2: 监控整个副本集

```bash
mongostat --discover
```

## 关联命令

- [[mongotop]]
- [[mongosh]]

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
