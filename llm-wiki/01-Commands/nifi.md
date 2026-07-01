---
{
  "cmd_name": "nifi",
  "cmd_category": "大数据/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "参考 https://nifi.apache.org/docs/nifi-docs/html/getting-started.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "airflow",
    "kafka-connect"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/bigdata/extra.yaml"
}
---

# nifi

> Apache NiFi 数据流 CLI

## 安装

```bash
参考 https://nifi.apache.org/docs/nifi-docs/html/getting-started.html
```

## 用法

```
nifi [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--version` |  |
| `flow` | 导入/导出 |
| `pg-get-root` |  |

## 示例

### 示例 1: 导入数据流

```bash
nifi flow import --inputFile flow.json
```

### 示例 2: 获取根进程组 ID

```bash
nifi pg-get-root
```

## 关联命令

- [[airflow]]
- [[kafka-connect]]

## 风险提示

> ⚠️ **MEDIUM**: 导入/修改流程会改变数据流转，请在测试环境验证

## 所属维度

[[扩展工具-MOC|大数据/扩展工具]]
