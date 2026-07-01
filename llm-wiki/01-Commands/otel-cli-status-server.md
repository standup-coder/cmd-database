---
{
  "cmd_name": "otel-cli status server",
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

# otel-cli status server

> Check OpenTelemetry endpoint status

## 安装

```bash
Download from https://github.com/equinix-labs/otel-cli/releases
```

## 用法

```
otel-cli status server [endpoint]
```

## 示例

### 示例 1: Check server status

```bash
otel-cli status server localhost:4317
```

### 示例 2: Check HTTPS endpoint

```bash
otel-cli status server https://otlp.collector:4318
```

### 示例 3: Check with timeout

```bash
otel-cli status server localhost:4317 --timeout 5s
```

## 风险提示

> ⚠️ **LOW**: Read-only status check

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
