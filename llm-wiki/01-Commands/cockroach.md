---
{
  "cmd_name": "cockroach",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://www.cockroachlabs.com/docs/stable/install-cockroachdb-linux",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "psql",
    "tidb-ctl"
  ],
  "cmd_tags": [
    "data",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# cockroach

> CockroachDB 分布式 SQL 数据库 CLI

## 安装

```bash
参考 https://www.cockroachlabs.com/docs/stable/install-cockroachdb-linux
```

## 用法

```
cockroach [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `sql` | 启动 SQL shell |
| `init` | 初始化集群 |
| `node` | 管理节点 |
| `start` | 启动节点 |

## 示例

### 示例 1: 连接不安全模式集群

```bash
cockroach sql --insecure
```

### 示例 2: 初始化集群

```bash
cockroach init --insecure --host=node1
```

## 关联命令

- [[psql]]
- [[tidb-ctl]]

## 风险提示

> ⚠️ **HIGH**: init 和节点管理操作会影响整个集群，请在测试环境验证

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
