---
{
  "cmd_name": "scylla",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://opensource.docs.scylladb.com/stable/getting-started/installation.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cqlsh",
    "cassandra-stress"
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

# scylla

> ScyllaDB 高性能 Cassandra 兼容数据库

## 安装

```bash
参考 https://opensource.docs.scylladb.com/stable/getting-started/installation.html
```

## 用法

```
scylla [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--version` |  |
| `--workdir` |  |
| `--options-file` |  |

## 示例

### 示例 1: 查看版本

```bash
scylla --version
```

### 示例 2: 启动 Scylla 服务

```bash
sudo systemctl start scylla-server
```

## 关联命令

- [[cqlsh]]
- [[cassandra-stress]]

## 风险提示

> ⚠️ **MEDIUM**: Scylla 是系统级服务，启动前请确认资源配置

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
