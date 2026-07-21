---
{
  "cmd_name": "grafana-cli plugins install",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Installed with Grafana",
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

# grafana-cli plugins install

> Install Grafana plugin

## 安装

```bash
Installed with Grafana
```

## 用法

```
grafana-cli plugins install [plugin-id]
```

## 示例

### 示例 1: Install pie chart panel plugin

```bash
grafana-cli plugins install grafana-piechart-panel
```

### 示例 2: Install Kubernetes monitoring app

```bash
grafana-cli plugins install grafana-kubernetes-app
```

### 示例 3: Install clock panel plugin

```bash
grafana-cli plugins install grafana-clock-panel
```

## 风险提示

> ⚠️ **MEDIUM**: Installing plugins modifies Grafana configuration

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
