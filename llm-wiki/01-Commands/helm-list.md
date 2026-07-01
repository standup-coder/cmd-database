---
{
  "cmd_name": "helm list",
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

# helm list

> List Helm releases

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Filter by namespace |
| `-A` | List releases across all namespaces |
| `-a` | Show all releases (including uninstalled) |
| `-o` | Output format: table, json, yaml |
| `--filter` | Filter releases by regex pattern |

## 示例

### 示例 1: List releases in default namespace

```bash
helm list
```

### 示例 2: List all releases in all namespaces

```bash
helm list -A
```

### 示例 3: List releases in production namespace

```bash
helm list -n production
```

### 示例 4: Show all releases including uninstalled

```bash
helm list -a
```

### 示例 5: Filter releases by name pattern

```bash
helm list --filter 'nginx'
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists releases only

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
