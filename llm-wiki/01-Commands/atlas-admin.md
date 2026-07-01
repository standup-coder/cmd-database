---
{
  "cmd_name": "atlas-admin",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "随 Apache Atlas 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "hive",
    "kafka"
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

# atlas-admin

> Apache Atlas 元数据管理命令

## 安装

```bash
随 Apache Atlas 安装
```

## 用法

```
atlas-admin [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-import` |  |
| `-export` |  |
| `-status` |  |

## 示例

### 示例 1: 查看 Atlas 状态

```bash
bin/atlas_admin.py -status
```

### 示例 2: 导入元数据

```bash
bin/import-export.py -i metadata.json
```

## 关联命令

- [[hive]]
- [[kafka]]

## 风险提示

> ⚠️ **MEDIUM**: 导入导出元数据会影响数据目录，请确认内容

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
