---
{
  "cmd_name": "trivy fs",
  "cmd_category": "Kubernetes Security",
  "cmd_dimension": "Kubernetes Security",
  "cmd_install": "Download from https://aquasecurity.github.io/trivy/",
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
  "source_file": "data/container/k8s/k8s-security.yaml"
}
---

# trivy fs

> Scan filesystem for vulnerabilities and misconfigurations

## 安装

```bash
Download from https://aquasecurity.github.io/trivy/
```

## 用法

```
trivy fs [path] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--security-checks` | Security checks: vuln, config, secret |
| `--severity` | Filter by severity |

## 示例

### 示例 1: Scan current directory

```bash
trivy fs .
```

### 示例 2: Scan for vulnerabilities and misconfigurations

```bash
trivy fs --security-checks vuln,config /path/to/project
```

### 示例 3: Scan for critical issues only

```bash
trivy fs --severity CRITICAL /app
```

## 风险提示

> ⚠️ **LOW**: Read-only scanning; no file modifications

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
