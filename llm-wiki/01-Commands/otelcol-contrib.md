---
{
  "cmd_name": "otelcol-contrib",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Download from https://github.com/open-telemetry/opentelemetry-collector-contrib/releases",
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

# otelcol-contrib

> Start OpenTelemetry Collector Contrib distribution

## 安装

```bash
Download from https://github.com/open-telemetry/opentelemetry-collector-contrib/releases
```

## 用法

```
otelcol-contrib [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | Configuration file path |
| `--feature-gates` | Enable experimental features |

## 示例

### 示例 1: Start contrib collector

```bash
otelcol-contrib --config=config.yaml
```

### 示例 2: Start with feature gates

```bash
otelcol-contrib --config=config.yaml --feature-gates=telemetry.useOtelForInternalMetrics
```

### 示例 3: Start with custom scrape config

```bash
otelcol-contrib --config=config.yaml --set=receivers.prometheus.config.scrape_configs[0].job_name=otel
```

## 风险提示

> ⚠️ **MEDIUM**: Contrib version includes experimental features

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
