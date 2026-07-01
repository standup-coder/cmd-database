---
{
  "cmd_name": "amtool check-config",
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
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-monitor.yaml"
}
---

# amtool check-config

> Validate Alertmanager configuration

## 安装

```bash
Installed with Alertmanager
```

## 用法

```
amtool check-config [config-file]
```

## 示例

### 示例 1: Validate Alertmanager config

```bash
amtool check-config alertmanager.yml
```

### 示例 2: Validate against running instance

```bash
amtool check-config --alertmanager.url=http://localhost:9093 alertmanager.yml
```

### 示例 3: Check routing configuration

```bash
amtool check-config --check-routing alertmanager.yml
```

## 风险提示

> ⚠️ **LOW**: Read-only validation

## 所属维度

[[Kubernetes Monitoring  Logging-MOC|Kubernetes Monitoring & Logging]]
