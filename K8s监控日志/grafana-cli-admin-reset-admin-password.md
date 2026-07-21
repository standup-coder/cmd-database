---
{
  "cmd_name": "grafana-cli admin reset-admin-password",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Installed with Grafana",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# grafana-cli admin reset-admin-password

> Reset Grafana admin password

## 安装

```bash
Installed with Grafana
```

## 用法

```
grafana-cli admin reset-admin-password [new-password]
```

## 示例

### 示例 1: Reset admin password

```bash
grafana-cli admin reset-admin-password newpassword123
```

### 示例 2: Reset with custom home path

```bash
grafana-cli admin reset-admin-password --homepath=/usr/share/grafana newpass
```

### 示例 3: Reset with custom config

```bash
grafana-cli admin reset-admin-password --config=/etc/grafana/grafana.ini newpass
```

## 风险提示

> ⚠️ **HIGH**: Resets admin password; security-sensitive operation

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
