---
cmd_name: istioctl proxy-status
cmd_category: "容器编排/K8s网络插件"
cmd_dimension: Kubernetes Networking
cmd_install: Istio service mesh installation
cmd_platforms:
- linux
- darwin
- windows
summary: "Check Envoy proxy status in service mesh"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-network.yaml
---


# istioctl proxy-status

> Check Envoy proxy status in service mesh

## 安装

```bash
Istio service mesh installation
```

## 用法

```
istioctl proxy-status [pod-name] [flags]
```

## 示例

### 示例 1: List status of all Envoy proxies

```bash
istioctl proxy-status
```

### 示例 2: Check specific proxy status

```bash
istioctl proxy-status myapp-pod-123456-abcde
```

### 示例 3: Check proxies in production namespace

```bash
istioctl proxy-status --namespace production
```

## 风险提示

> ⚠️ **LOW**: Read-only status check; shows proxy health

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
