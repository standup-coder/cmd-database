---
{
  "cmd_name": "helm search repo",
  "cmd_category": "Kubernetes Helm Package Management",
  "cmd_dimension": "Kubernetes Helm Package Management",
  "cmd_install": "Download from https://helm.sh/docs/intro/install/",
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
  "source_file": "data/container/k8s/k8s-helm-enhanced.yaml"
}
---

# helm search repo

> Search for charts in repositories

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm search repo [keyword] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--versions` | Show all versions of charts |
| `--version` | Specific version to search for |
| `-l` | Show long listing format |

## 示例

### 示例 1: Search for nginx charts

```bash
helm search repo nginx
```

### 示例 2: Show all versions of nginx charts

```bash
helm search repo nginx --versions
```

### 示例 3: Search for database charts with detailed info

```bash
helm search repo database -l
```

## 风险提示

> ⚠️ **LOW**: Read-only search operation

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
