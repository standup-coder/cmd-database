---
cmd_name: kubectl apply
cmd_category: "容器编排/Kubernetes命令"
cmd_dimension: Container Orchestration
cmd_install: Download from https://kubernetes.io/docs/tasks/tools/
cmd_platforms:
- linux
- darwin
- windows
summary: "Apply a configuration to a resource by filename or stdin"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/container/kubernetes.yaml
---


# kubectl apply

> Apply a configuration to a resource by filename or stdin

## 安装

```bash
Download from https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl apply -f [filename]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Filename, directory, or URL to files |
| `-n` | Target namespace |
| `--dry-run` | Preview changes without applying |
| `-R` | Process directory recursively |

## 示例

### 示例 1: Apply configuration from file

```bash
kubectl apply -f deployment.yaml
```

### 示例 2: Apply configuration from URL

```bash
kubectl apply -f https://example.com/config.yaml
```

### 示例 3: Apply all configs in directory

```bash
kubectl apply -f ./configs/
```

### 示例 4: Preview changes without applying

```bash
kubectl apply -f deployment.yaml --dry-run=client
```

## 风险提示

> ⚠️ **HIGH**: Modifies cluster resources; can cause service disruption

## 所属维度

[[Kubernetes命令-MOC|Container Orchestration]]
