---
{
  "cmd_name": "systemctl status promtail",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Built-in systemd command",
  "cmd_platforms": [
    "linux"
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

# systemctl status promtail

> Check Promtail service status

## 安装

```bash
Built-in systemd command
```

## 用法

```
systemctl status promtail
```

## 示例

### 示例 1: View Promtail service status

```bash
systemctl status promtail
```

### 示例 2: Start Promtail service

```bash
systemctl start promtail
```

### 示例 3: Restart Promtail service

```bash
systemctl restart promtail
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no risks

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
