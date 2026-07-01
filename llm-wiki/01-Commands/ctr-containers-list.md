---
{
  "cmd_name": "ctr containers list",
  "cmd_category": "Kubernetes Container Runtime",
  "cmd_dimension": "Kubernetes Container Runtime",
  "cmd_install": "Installed with containerd",
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
  "source_file": "data/container/k8s/k8s-runtime.yaml"
}
---

# ctr containers list

> List containers in containerd

## 安装

```bash
Installed with containerd
```

## 用法

```
ctr containers list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-q` | Print only container IDs |

## 示例

### 示例 1: List all containerd containers

```bash
ctr containers list
```

### 示例 2: List containers in k8s.io namespace

```bash
ctr -n k8s.io containers list
```

### 示例 3: List only container IDs

```bash
ctr containers list -q
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists containers only

## 所属维度

[[Kubernetes Container Runtime-MOC|Kubernetes Container Runtime]]
