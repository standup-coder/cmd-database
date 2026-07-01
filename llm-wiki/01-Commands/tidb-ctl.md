---
{
  "cmd_name": "tidb-ctl",
  "cmd_category": "数据库工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://docs.pingcap.com/tidb/stable/tidb-control",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mysql",
    "cockroach"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/extra.yaml"
}
---

# tidb-ctl

> TiDB 集群诊断与管理工具

## 安装

```bash
参考 https://docs.pingcap.com/tidb/stable/tidb-control
```

## 用法

```
tidb-ctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `schema` | 查看 schema |
| `region` | 查看 region |
| `etcd` | 查看 etcd |

## 示例

### 示例 1: 查看 mysql 数据库 schema

```bash
tidb-ctl schema in mysql
```

### 示例 2: 查看 region 信息

```bash
tidb-ctl region -i 1
```

## 关联命令

- [[mysql]]
- [[cockroach]]

## 风险提示

> ⚠️ **MEDIUM**: 直接操作 TiDB 内部元数据可能导致不一致，请谨慎

## 所属维度

[[扩展工具-MOC|数据库工具/扩展工具]]
