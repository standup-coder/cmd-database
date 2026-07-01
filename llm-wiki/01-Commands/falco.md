---
{
  "cmd_name": "falco",
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

# falco

> Start Falco runtime security monitoring

## 安装

```bash
Install from https://falco.org/docs/getting-started/installation/
```

## 用法

```
falco [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | Configuration file path |
| `-r` | Rules file path |
| `-M` | Run for this many seconds then exit |

## 示例

### 示例 1: Start Falco with config file

```bash
falco -c /etc/falco/falco.yaml
```

### 示例 2: Load custom security rules

```bash
falco -r /etc/falco/rules/custom-rules.yaml
```

### 示例 3: Run Falco for 60 seconds

```bash
falco -M 60
```

## 风险提示

> ⚠️ **LOW**: Monitoring only; detects security events without blocking

## 所属维度

[[Kubernetes Security-MOC|Kubernetes Security]]
