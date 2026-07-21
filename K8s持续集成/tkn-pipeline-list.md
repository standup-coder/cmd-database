---
{
  "cmd_name": "tkn pipeline list",
  "cmd_category": "Kubernetes CI/CD",
  "cmd_dimension": "CD",
  "cmd_install": "Download from https://tekton.dev/docs/cli/",
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
  "source_file": "data/container/k8s/k8s-cicd.yaml"
}
---

# tkn pipeline list

> List Tekton pipelines

## 安装

```bash
Download from https://tekton.dev/docs/cli/
```

## 用法

```
tkn pipeline list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | Filter by namespace |
| `-A` | List across all namespaces |

## 示例

### 示例 1: List pipelines in current namespace

```bash
tkn pipeline list
```

### 示例 2: List pipelines in all namespaces

```bash
tkn pipeline list -A
```

### 示例 3: List pipelines in cicd namespace

```bash
tkn pipeline list -n cicd
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists pipelines only

## 所属维度

[[K8s持续集成-MOC|Kubernetes CI/CD]]
