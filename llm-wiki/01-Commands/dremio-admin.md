---
{
  "cmd_name": "dremio-admin",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Dremio 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "presto",
    "hive"
  ],
  "cmd_tags": [
    "data",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/bigdata/more.yaml"
}
---

# dremio-admin

> Dremio 数据湖引擎管理工具

## 安装

```bash
随 Dremio 安装
```

## 用法

```
dremio-admin [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `backup` | 备份 |
| `restore` | 恢复 |
| `set-password` |  |

## 示例

### 示例 1: 备份 Dremio

```bash
dremio-admin backup -f /backup/dremio.zip
```

### 示例 2: 恢复

```bash
dremio-admin restore -f /backup/dremio.zip
```

## 关联命令

- [[presto]]
- [[hive]]

## 风险提示

> ⚠️ **HIGH**: restore 会覆盖现有元数据，请确认备份来源

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
