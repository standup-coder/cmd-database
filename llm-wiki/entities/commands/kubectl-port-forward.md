---
cmd_name: kubectl port-forward
cmd_category: "容器编排/K8s故障排查"
cmd_dimension: Kubernetes Troubleshooting
cmd_install: kubectl 内置命令
cmd_platforms:
- linux
- darwin
- windows
summary: "端口转发用于本地调试和测试"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/container/k8s-troubleshooting.yaml
---


# kubectl port-forward

> 端口转发用于本地调试和测试

## 安装

```bash
kubectl 内置命令
```

## 用法

```
kubectl port-forward [pod/service] [local-port]:[remote-port]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n` | 指定命名空间 |
| `--address` | 监听地址 |

## 示例

### 示例 1: 将服务端口转发到本地

```bash
kubectl port-forward svc/myapp 8080:80
```

### 示例 2: 转发调试端口用于远程调试

```bash
kubectl port-forward pod/mypod 9229:9229
```

### 示例 3: 允许外部访问的端口转发

```bash
kubectl port-forward svc/database 3306:3306 --address 0.0.0.0
```

## 风险提示

> ⚠️ **MEDIUM**: 暴露内部服务到本地网络

## 所属维度

[[K8s故障排查-MOC|Kubernetes Troubleshooting]]
