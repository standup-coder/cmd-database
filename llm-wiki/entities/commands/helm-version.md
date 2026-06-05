---
cmd_name: helm version
cmd_category: "容器编排/K8s Helm包管理"
cmd_dimension: Kubernetes Helm Package Management
cmd_install: Download from https://helm.sh/docs/intro/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "Display Helm client and server version"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-helm-enhanced.yaml
---


# helm version

> Display Helm client and server version

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm version [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--short` | Show short version only |
| `--template` | Template for custom output format |

## 示例

### 示例 1: Show client and server versions

```bash
helm version
```

### 示例 2: Show short version information

```bash
helm version --short
```

### 示例 3: Show client version only

```bash
helm version --template '{{.Client.SemVer}}'
```

## 风险提示

> ⚠️ **LOW**: Version information only

## 所属维度

[[K8s Helm包管理-MOC|Kubernetes Helm Package Management]]
