---
{
  "cmd_name": "airbyte",
  "cmd_category": "大数据/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "参考 https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "fivetran",
    "airflow",
    "dbt"
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

# airbyte

> Airbyte 数据集成平台 CLI

## 安装

```bash
参考 https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart
```

## 用法

```
airbyte [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `local` | 本地部署 |
| `status` |  |
| `connections` |  |

## 示例

### 示例 1: 本地部署 Airbyte

```bash
airbyte local deploy
```

### 示例 2: 查看状态

```bash
airbyte status
```

## 关联命令

- [[airflow]]
- [[dbt]]

## 风险提示

> ⚠️ **MEDIUM**: 连接源和目标会涉及凭据，请使用 Secret 管理

## 所属维度

[[扩展命令-MOC|大数据/扩展命令]]
