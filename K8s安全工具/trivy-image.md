---
{
  "cmd_name": "trivy image",
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

# trivy image

> Scan container image for vulnerabilities

## 安装

```bash
Download from https://aquasecurity.github.io/trivy/
```

## 用法

```
trivy image [image-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--severity` | Filter by severity: CRITICAL,HIGH,MEDIUM,LOW |
| `--format` | Output format: table, json, sarif |
| `--exit-code` | Exit with code 1 if vulnerabilities found |

## 示例

### 示例 1: Scan nginx image for vulnerabilities

```bash
trivy image nginx:latest
```

### 示例 2: Scan for high and critical vulnerabilities only

```bash
trivy image --severity HIGH,CRITICAL nginx:latest
```

### 示例 3: Output scan results in JSON format

```bash
trivy image --format json nginx:latest
```

### 示例 4: Scan and fail if vulnerabilities found

```bash
trivy image --exit-code 1 myapp:v1.0
```

## 风险提示

> ⚠️ **LOW**: Read-only scanning; no modifications to images

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
