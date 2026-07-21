---
{
  "cmd_name": "grafana-cli plugins list-remote",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# grafana-cli plugins list-remote

> List available Grafana plugins

## 安装

```bash
Installed with Grafana
```

## 用法

```
grafana-cli plugins list-remote
```

## 示例

### 示例 1: List all available plugins

```bash
grafana-cli plugins list-remote
```

### 示例 2: Search for Kubernetes-related plugins

```bash
grafana-cli plugins list-remote | grep kubernetes
```

### 示例 3: List panel plugins

```bash
grafana-cli plugins list-remote | grep panel
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists available plugins

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
