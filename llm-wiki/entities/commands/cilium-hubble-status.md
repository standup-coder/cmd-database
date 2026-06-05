---
cmd_name: cilium hubble status
cmd_category: "容器编排/K8s网络插件"
cmd_dimension: Kubernetes Networking
cmd_install: Installed with Cilium Hubble
cmd_platforms:
- linux
summary: "Check Hubble observability status"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-network.yaml
---


# cilium hubble status

> Check Hubble observability status

## 安装

```bash
Installed with Cilium Hubble
```

## 用法

```
cilium hubble status
```

## 示例

### 示例 1: Display Hubble status

```bash
cilium hubble status
```

### 示例 2: Observe network flows in real-time

```bash
hubble observe
```

### 示例 3: Observe flows in specific namespace

```bash
hubble observe --namespace default
```

## 风险提示

> ⚠️ **LOW**: Read-only observation; no operational impact

## 所属维度

[[K8s网络插件-MOC|Kubernetes Networking]]
