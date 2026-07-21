---
{
  "cmd_name": "otelcol",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Download from https://github.com/open-telemetry/opentelemetry-collector/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# otelcol

> Start OpenTelemetry Collector

## 安装

```bash
Download from https://github.com/open-telemetry/opentelemetry-collector/releases
```

## 用法

```
otelcol [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | Configuration file path |
| `--set` | Set property value |

## 示例

### 示例 1: Start with config file

```bash
otelcol --config=config.yaml
```

### 示例 2: Start with debug logging

```bash
otelcol --config=config.yaml --set=service.telemetry.logs.level=debug
```

### 示例 3: Start with custom endpoint

```bash
otelcol --config=config.yaml --set=receivers.otlp.protocols.grpc.endpoint=0.0.0.0:4317
```

## 风险提示

> ⚠️ **MEDIUM**: Incorrect config may lose telemetry data

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
