---
cmd_name: systemctl status prometheus
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Built-in systemd command
cmd_platforms:
- linux
summary: "Check Prometheus service status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# systemctl status prometheus

> Check Prometheus service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status prometheus
```

## 示例

### 示例 1: View Prometheus service status

```bash
systemctl status prometheus
```

### 示例 2: Start Prometheus service

```bash
systemctl start prometheus
```

### 示例 3: Restart Prometheus service

```bash
systemctl restart prometheus
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
