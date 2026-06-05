---
cmd_name: grafana-server
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Download from https://grafana.com/grafana/download
cmd_platforms:
- linux
- darwin
- windows
summary: "Start Grafana visualization server"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# grafana-server

> Start Grafana visualization server

## 安装

```bash
Download from https://grafana.com/grafana/download
```

## 用法

```
grafana-server [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | Configuration file path |
| `--homepath` | Grafana home directory |

## 示例

### 示例 1: Start with default settings

```bash
grafana-server
```

### 示例 2: Start with custom config

```bash
grafana-server --config=/etc/grafana/grafana.ini
```

### 示例 3: Start with custom home path

```bash
grafana-server --homepath=/usr/share/grafana
```

## 风险提示

> ⚠️ **MEDIUM**: Ensure proper authentication configured

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
