---
{
  "cmd_name": "tempo-cli",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://grafana.com/docs/tempo/latest/setup/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "jaeger-cli",
    "otelcol"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# tempo-cli

> Grafana Tempo 追踪查询 CLI

## 安装

```bash
参考 https://grafana.com/docs/tempo/latest/setup/
```

## 用法

```
tempo-cli [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--server` | 地址 |
| `query` | 查询 trace |

## 示例

### 示例 1: 查询 trace ID

```bash
tempo-cli query 123e4567
```

### 示例 2: 搜索 span

```bash
tempo-cli --server http://tempo:3200 search 'name=GET /api'
```

## 关联命令

- [[jaeger-cli]]
- [[otelcol]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
