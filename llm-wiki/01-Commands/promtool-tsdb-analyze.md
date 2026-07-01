---
{
  "cmd_name": "promtool tsdb analyze",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Installed with Prometheus",
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

# promtool tsdb analyze

> Analyze Prometheus TSDB blocks

## 安装

```bash
Installed with Prometheus
```

## 用法

```
promtool tsdb analyze [db-path]
```

## 示例

### 示例 1: Analyze TSDB database

```bash
promtool tsdb analyze /data/prometheus
```

### 示例 2: Analyze with result limit

```bash
promtool tsdb analyze --limit=20 /data/prometheus
```

### 示例 3: Extended analysis with more details

```bash
promtool tsdb analyze --extended /data/prometheus
```

## 风险提示

> ⚠️ **LOW**: Read-only analysis; no modifications

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
