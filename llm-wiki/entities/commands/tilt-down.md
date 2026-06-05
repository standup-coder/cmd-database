---
cmd_name: tilt down
cmd_category: "容器编排/K8s开发调试"
cmd_dimension: Kubernetes Development
cmd_install: Download from https://docs.tilt.dev/install.html
cmd_platforms:
- linux
- darwin
- windows
summary: "Stop Tilt and cleanup resources"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-dev.yaml
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

## 风险提示

> ⚠️ **MEDIUM**: Deletes deployed resources from cluster

## 所属维度

[[K8s开发调试-MOC|Kubernetes Development]]
