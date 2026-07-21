---
{
  "cmd_name": "mongoexport",
  "cmd_category": "数据库工具/NoSQL",
  "cmd_dimension": "NoSQL",
  "cmd_install": "随 MongoDB Database Tools 安装",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mongosh",
    "mongodump"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/nosql.yaml"
}
---

# mongoexport

> 将 MongoDB 集合导出为 JSON 或 CSV

## 安装

```bash
随 MongoDB Database Tools 安装
```

## 用法

```
mongoexport [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--uri` | MongoDB 连接 URI |
| `--collection` | 指定集合 |
| `--out` | 输出文件 |

## 示例

### 示例 1: 导出集合为 JSON

```bash
mongoexport --uri="mongodb://localhost:27017/mydb" --collection users --out users.json
```

### 示例 2: 导出指定字段为 CSV

```bash
mongoexport --collection users --type=csv --fields=name,email --out users.csv
```

## 关联命令

- [[mongosh]]
- [[mongodump]]

## 风险提示

> ⚠️ **MEDIUM**: 导出的文件可能包含敏感信息，请妥善保管存储位置

## 所属维度

[[NoSQL-MOC|数据库工具/NoSQL]]
