---
cmd_name: helm status
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Display status of Helm release"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm status

> Display status of Helm release

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm status [release-name] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Release namespace |
| `-o` | Output format: table, json, yaml |
| `--show-resources` | Show deployed resources |

## 示例

### 示例 1: Show nginx release status

```bash
helm status nginx
```

### 示例 2: Show status of release in production

```bash
helm status nginx -n production
```

### 示例 3: Show status in YAML format

```bash
helm status nginx -o yaml
```

### 示例 4: Show deployed resources

```bash
helm status nginx --show-resources
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; displays status only

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
