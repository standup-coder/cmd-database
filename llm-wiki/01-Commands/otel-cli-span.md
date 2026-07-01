---
{
  "cmd_name": "otel-cli span",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Download from https://github.com/equinix-labs/otel-cli/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "rlhf",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# otel-cli span

> Send span data to OpenTelemetry endpoint

## 安装

```bash
Download from https://github.com/equinix-labs/otel-cli/releases
```

## 用法

```
otel-cli span [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--endpoint` | OTLP endpoint URL |
| `--service` | Service name |
| `--name` | Span name |

## 示例

### 示例 1: Send simple span

```bash
otel-cli span --endpoint localhost:4317 --service myapp --name myspan
```

### 示例 2: Send span with attributes

```bash
otel-cli span --endpoint localhost:4317 --service myapp --name operation --attrs key=value
```

### 示例 3: Send background span

```bash
otel-cli span background --endpoint localhost:4317 --service myapp --name background-job
```

## 风险提示

> ⚠️ **LOW**: Sends telemetry data only

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
