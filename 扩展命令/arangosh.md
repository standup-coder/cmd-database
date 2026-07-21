---
{
  "cmd_name": "arangosh",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 ArangoDB 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cypher-shell",
    "mongosh"
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

# arangosh

> ArangoDB 多模型数据库 Shell

## 安装

```bash
随 ArangoDB 安装
```

## 用法

```
arangosh [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server.endpoint` |  |
| `--server.username` |  |
| `--javascript.execute` |  |

## 示例

### 示例 1: 连接 ArangoDB

```bash
arangosh --server.endpoint tcp://localhost:8529
```

### 示例 2: 执行 JS 脚本

```bash
arangosh --javascript.execute script.js
```

## 关联命令

- [[cypher-shell]]
- [[mongosh]]

## 风险提示

> ⚠️ **MEDIUM**: JS 脚本可删除数据库，请确认脚本内容

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
