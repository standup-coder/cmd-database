---
{
  "cmd_name": "mongotop",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongostat",
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

# mongotop

> 实时显示 MongoDB 集合级读写时间

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongotop [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--host` | 主机 |
| `--locks` | 显示锁信息 |
| `--sleep` | 采样间隔 |

## 示例

### 示例 1: 每 5 秒采样一次

```bash
mongotop 5
```

### 示例 2: 监控副本集

```bash
mongotop --host rs0/mongo1:27017
```

## 关联命令

- [[mongostat]]
- [[mongosh]]

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
