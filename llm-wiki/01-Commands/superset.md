---
{
  "cmd_name": "superset",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "pip install apache-superset",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "metabase",
    "dbt"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# superset

> Apache Superset 数据可视化平台

## 安装

```bash
pip install apache-superset
```

## 用法

```
superset [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `db` | upgrade 升级元数据库 |
| `fab` | create-admin |
| `run` | -p 端口 |
| `load_examples` |  |

## 示例

### 示例 1: 升级元数据库

```bash
superset db upgrade
```

### 示例 2: 开发模式启动

```bash
superset run -p 8088 --with-threads --reload --debugger
```

## 关联命令

- [[metabase]]
- [[dbt]]

## 风险提示

> ⚠️ **MEDIUM**: 生产环境请关闭 debugger 和 reload，并配置认证

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
