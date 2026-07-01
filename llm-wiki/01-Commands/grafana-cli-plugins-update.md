---
{
  "cmd_name": "grafana-cli plugins update",
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

# grafana-cli plugins update

> Update Grafana plugin

## 安装

```bash
Installed with Grafana
```

## 用法

```
grafana-cli plugins update [plugin-id]
```

## 示例

### 示例 1: Update specific plugin

```bash
grafana-cli plugins update grafana-piechart-panel
```

### 示例 2: Update all installed plugins

```bash
grafana-cli plugins update-all
```

### 示例 3: Update Kubernetes app plugin

```bash
grafana-cli plugins update grafana-kubernetes-app
```

## 风险提示

> ⚠️ **MEDIUM**: Plugin updates may break dashboards

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
