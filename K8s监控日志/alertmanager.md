---
{
  "cmd_name": "alertmanager",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Download from https://prometheus.io/download/",
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

# alertmanager

> Start Prometheus Alertmanager

## 安装

```bash
Download from https://prometheus.io/download/
```

## 用法

```
alertmanager [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config.file` | Alertmanager configuration file |
| `--web.listen-address` | Listen address for web interface |
| `--storage.path` | Base path for data storage |

## 示例

### 示例 1: Start Alertmanager with config

```bash
alertmanager --config.file=alertmanager.yml
```

### 示例 2: Start on specific port

```bash
alertmanager --config.file=alertmanager.yml --web.listen-address=:9093
```

### 示例 3: Start with custom storage

```bash
alertmanager --config.file=alertmanager.yml --storage.path=/data/alertmanager
```

## 风险提示

> ⚠️ **MEDIUM**: Incorrect config affects alert routing

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
