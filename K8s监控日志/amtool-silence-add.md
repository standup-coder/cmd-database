---
{
  "cmd_name": "amtool silence add",
  "cmd_category": "Kubernetes Monitoring & Logging",
  "cmd_dimension": "Kubernetes Monitoring  Logging",
  "cmd_install": "Installed with Alertmanager",
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

# amtool silence add

> Add silence to Alertmanager

## 安装

```bash
Installed with Alertmanager
```

## 用法

```
amtool silence add [matcher] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--duration` | Silence duration |
| `--comment` | Silence comment |

## 示例

### 示例 1: Silence alert for 2 hours

```bash
amtool silence add alertname=HighCPU --duration=2h --comment='Maintenance'
```

### 示例 2: Silence warning alerts

```bash
amtool silence add severity=warning --duration=1h
```

### 示例 3: Silence instance alerts

```bash
amtool silence add instance=server1 --duration=30m --comment='Upgrade'
```

## 风险提示

> ⚠️ **MEDIUM**: Silencing alerts may mask issues

## 所属维度

[[K8s监控日志-MOC|Kubernetes Monitoring & Logging]]
