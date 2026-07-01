---
{
  "cmd_name": "kubectl-neat",
  "cmd_category": "容器编排/K8s辅助工具",
  "cmd_dimension": "K8s辅助工具",
  "cmd_install": "kubectl krew install neat",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "kustomize"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# kubectl-neat

> 移除 kubectl get 输出中的默认字段，使 YAML 更简洁

## 安装

```bash
kubectl krew install neat
```

## 用法

```
kubectl neat [OPTIONS]
```

## 示例

### 示例 1: 获取精简后的 Pod YAML

```bash
kubectl get pod mypod -o yaml | kubectl neat
```

### 示例 2: 精简本地 YAML 文件

```bash
kubectl neat -f deploy.yaml -o yaml
```

## 关联命令

- [[kubectl]]
- [[kustomize]]

## 风险提示

> ⚠️ **LOW**: 只读/格式化工具，不会修改集群

## 所属维度

[[K8s辅助工具-MOC|容器编排/K8s辅助工具]]
