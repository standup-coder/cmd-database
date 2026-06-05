---
cmd_name: kubectl port-forward svc/istio-ingressgateway
cmd_category: "容器编排/K8s机器学习运维"
cmd_dimension: Kubernetes MLOps
cmd_install: Requires Kubeflow with Istio deployed
cmd_platforms:
- linux
- darwin
- windows
summary: "Access Kubeflow dashboard locally"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-mlops.yaml
---


# kubectl port-forward svc/istio-ingressgateway

> Access Kubeflow dashboard locally

## 安装

```bash
Requires Kubeflow with Istio deployed
```

## 用法

```
kubectl port-forward svc/istio-ingressgateway <local-port>:80 -n istio-system
```

## 示例

### 示例 1: Forward Kubeflow dashboard to localhost:8080

```bash
kubectl port-forward svc/istio-ingressgateway 8080:80 -n istio-system
```

## 风险提示

> ⚠️ **LOW**: Local port forwarding only

## 所属维度

[[K8s机器学习运维-MOC|Kubernetes MLOps]]
