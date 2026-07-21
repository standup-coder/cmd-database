---
{
  "cmd_name": "kubectl",
  "cmd_category": "容器编排/Kubernetes命令",
  "cmd_dimension": "Kubernetes命令",
  "cmd_install": "参考 https://kubernetes.io/docs/tasks/tools/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl get",
    "kubectl apply",
    "helm"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/kubernetes.yaml"
}
---

# kubectl

> Kubernetes命令行工具，管理集群资源

## 安装

```bash
参考 https://kubernetes.io/docs/tasks/tools/
```

## 用法

```
kubectl [命令] [类型] [名称] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--namespace, -n` | 指定命名空间 |
| `--context` | 指定kubeconfig上下文 |
| `--kubeconfig` | 指定kubeconfig文件路径 |
| `-o wide` | 显示更多列信息 |
| `-o yaml` | 以YAML格式输出 |
| `-o json` | 以JSON格式输出 |

## 示例

### 示例 1: 查看所有节点

```bash
kubectl get nodes
```

### 示例 2: 查看kube-system命名空间的Pod

```bash
kubectl get pods -n kube-system
```

### 示例 3: 查看Pod详细信息

```bash
kubectl describe pod mypod
```

### 示例 4: 应用YAML配置文件

```bash
kubectl apply -f deployment.yaml
```

## 关联命令

- [[kubectl-get]]
- [[kubectl-apply]]

## 所属维度

[[Kubernetes命令-MOC|容器编排/Kubernetes命令]]
