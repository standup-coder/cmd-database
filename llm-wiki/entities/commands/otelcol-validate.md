---
cmd_name: otelcol validate
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Installed with OpenTelemetry Collector
cmd_platforms:
- linux
- darwin
- windows
summary: "Validate OpenTelemetry Collector configuration"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# otelcol validate

> Validate OpenTelemetry Collector configuration

## 安装

```bash
Installed with OpenTelemetry Collector
```

## 用法

```
otelcol validate --config [config-file]
```

## 示例

### 示例 1: Validate configuration file

```bash
otelcol validate --config=config.yaml
```

### 示例 2: Validate with overrides

```bash
otelcol validate --config=config.yaml --set=service.telemetry.logs.level=debug
```

### 示例 3: Validate multiple configs

```bash
otelcol validate --config=*.yaml
```

## 风险提示

> ⚠️ **LOW**: Read-only validation

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
