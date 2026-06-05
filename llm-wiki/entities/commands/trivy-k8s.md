---
cmd_name: trivy k8s
cmd_category: "容器编排/K8s安全工具"
cmd_dimension: Kubernetes Security
cmd_install: Download from https://aquasecurity.github.io/trivy/
cmd_platforms:
- linux
- darwin
- windows
summary: "Scan Kubernetes cluster for security issues"
cmd_level: advanced
cmd_related: []
cmd_tags:
- kubernetes
- advanced
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-security.yaml
---


# trivy k8s

> Scan Kubernetes cluster for security issues

## 安装

```bash
Download from https://aquasecurity.github.io/trivy/
```

## 用法

```
trivy k8s [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace` | Scan specific namespace |
| `--report` | Report type: summary, all |

## 示例

### 示例 1: Scan entire cluster with summary

```bash
trivy k8s --report summary
```

### 示例 2: Scan production namespace

```bash
trivy k8s --namespace production
```

### 示例 3: Scan all resources in default namespace

```bash
trivy k8s all -n default
```

## 风险提示

> ⚠️ **LOW**: Read-only scanning; queries cluster via kubectl

## 所属维度

[[K8s安全工具-MOC|Kubernetes Security]]
