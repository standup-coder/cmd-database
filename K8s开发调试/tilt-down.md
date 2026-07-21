---
{
  "cmd_name": "tilt down",
  "cmd_category": "Kubernetes Development",
  "cmd_dimension": "Kubernetes Development",
  "cmd_install": "Download from https://docs.tilt.dev/install.html",
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
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-dev.yaml"
}
---

# tilt down

> Stop Tilt and cleanup resources

## 安装

```bash
Download from https://docs.tilt.dev/install.html
```

## 用法

```
tilt down
```

## 示例

### 示例 1: Stop Tilt and delete resources

```bash
tilt down
```

### 示例 2: 删除 Tilt 资源及创建的命名空间

```bash
tilt down --delete-namespaces
```

## 风险提示

> ⚠️ **MEDIUM**: Deletes deployed resources from cluster

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
