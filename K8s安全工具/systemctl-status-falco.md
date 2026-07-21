---
{
  "cmd_name": "systemctl status falco",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "Install from https://falco.org/docs/getting-started/installation/",
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
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# systemctl status falco

> Check Falco runtime security service status

## 安装

```bash
Install from https://falco.org/docs/getting-started/installation/
```

## 用法

```
systemctl status falco
```

## 示例

### 示例 1: View Falco service status

```bash
systemctl status falco
```

### 示例 2: Start Falco service

```bash
systemctl start falco
```

### 示例 3: Restart Falco service

```bash
systemctl restart falco
```

### 示例 4: Follow Falco security event logs

```bash
journalctl -u falco -f
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; no operational changes

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
