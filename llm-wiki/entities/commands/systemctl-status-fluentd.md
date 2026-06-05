---
cmd_name: systemctl status fluentd
cmd_category: "容器编排/K8s监控日志"
cmd_dimension: Kubernetes Monitoring  Logging
cmd_install: Built-in systemd command
cmd_platforms:
- linux
summary: "Check Fluentd service status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-monitor.yaml
---


# systemctl status fluentd

> Check Fluentd service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status fluentd
```

## 示例

### 示例 1: View Fluentd service status

```bash
systemctl status fluentd
```

### 示例 2: Start Fluentd service

```bash
systemctl start fluentd
```

### 示例 3: Restart Fluentd service

```bash
systemctl restart fluentd
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
