---
{
  "cmd_name": "jaeger-cli",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://www.jaegertracing.io/download/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "otelcol",
    "tempo-cli"
  ],
  "cmd_tags": [
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# jaeger-cli

> Jaeger 分布式追踪 CLI

## 安装

```bash
参考 https://www.jaegertracing.io/download/
```

## 用法

```
jaeger-cli [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--query.query-port` |  |
| `span` | 查询 |
| `trace` | 查询 |

## 示例

### 示例 1: 查询服务追踪

```bash
jaeger-cli query --service myservice
```

### 示例 2: 查看指定 trace

```bash
jaeger-cli trace 123e4567
```

## 关联命令

- [[otelcol]]
- [[tempo-cli]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
