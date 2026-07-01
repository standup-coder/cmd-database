---
{
  "cmd_name": "helm plugin list",
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

# helm plugin list

> List installed Helm plugins

## 安装

```bash
Download from https://helm.sh/docs/intro/install/
```

## 用法

```
helm plugin list
```

## 示例

### 示例 1: Show all installed plugins

```bash
helm plugin list
```

### 示例 2: Install helm-2to3 plugin

```bash
helm plugin install https://github.com/helm/helm-2to3
```

### 示例 3: Uninstall 2to3 plugin

```bash
helm plugin uninstall 2to3
```

## 风险提示

> ⚠️ **LOW**: Plugin management only

## 所属维度

[[Kubernetes Helm Package Management-MOC|Kubernetes Helm Package Management]]
