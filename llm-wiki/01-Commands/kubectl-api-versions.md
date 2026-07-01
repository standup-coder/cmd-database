---
{
  "cmd_name": "kubectl api-versions",
  "cmd_category": "Kubernetes Troubleshooting",
  "cmd_dimension": "Kubernetes Troubleshooting",
  "cmd_install": "kubectl 内置命令",
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
  "source_file": "data/container/k8s/k8s-troubleshooting.yaml"
}
---

# kubectl api-versions

> 显示支持的 API 版本

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl api-versions
```

## 示例

### 示例 1: 显示所有支持的 API 版本

```bash
kubectl api-versions
```

### 示例 2: 过滤显示 apps 相关 API 版本

```bash
kubectl api-versions | grep apps
```

## 风险提示

> ⚠️ **LOW**: 只读版本信息；无修改风险

## 所属维度

[[Kubernetes Troubleshooting-MOC|Kubernetes Troubleshooting]]
