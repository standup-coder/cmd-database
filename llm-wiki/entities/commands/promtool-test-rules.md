---
cmd_name: promtool test rules
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Installed with Prometheus
cmd_platforms:
- linux
- darwin
- windows
summary: "Test Prometheus alerting and recording rules"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# promtool test rules

> Test Prometheus alerting and recording rules

## 安装

```bash
Installed with Prometheus
```

## 用法

```
promtool test rules [test-file]
```

## 示例

### 示例 1: Run rule unit tests

```bash
promtool test rules test.yml
```

### 示例 2: Run all test files

```bash
promtool test rules tests/*.yml
```

### 示例 3: Run specific test

```bash
promtool test rules --run=TestCPUAlert test.yml
```

## 风险提示

> ⚠️ **LOW**: Testing rules only; no changes made

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
