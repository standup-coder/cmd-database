---
{
  "cmd_name": "metabase",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://www.metabase.com/start/oss/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "superset",
    "grafana"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# metabase

> 开源 BI 与数据探索平台

## 安装

```bash
参考 https://www.metabase.com/start/oss/
```

## 用法

```
metabase [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-Xmx` | 最大内存 |
| `-Dlog4j.configurationFile` |  |
| `--add-to-start` |  |

## 示例

### 示例 1: 启动 Metabase

```bash
java -jar metabase.jar
```

### 示例 2: 使用外部数据库

```bash
MB_DB_CONNECTION_URI='...' java -jar metabase.jar
```

## 关联命令

- [[superset]]

## 风险提示

> ⚠️ **MEDIUM**: Metabase 会连接数据库，请使用只读账户并限制权限

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
