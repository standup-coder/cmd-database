---
{
  "cmd_name": "promtool check config",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Installed with Prometheus or download from https://prometheus.io/download/",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# promtool check config

> Validate Prometheus configuration file

## 安装

```bash
Installed with Prometheus or download from https://prometheus.io/download/
```

## 用法

```
promtool check config [config-file]
```

## 示例

### 示例 1: Validate Prometheus configuration

```bash
promtool check config prometheus.yml
```

### 示例 2: Validate recording and alerting rules

```bash
promtool check rules rules/*.yml
```

### 示例 3: Check syntax only without validation

```bash
promtool check config --syntax-only prometheus.yml
```

## 风险提示

> ⚠️ **LOW**: Read-only validation; no operational impact

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
