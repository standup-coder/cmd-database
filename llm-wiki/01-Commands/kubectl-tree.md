---
{
  "cmd_name": "kubectl-tree",
  "cmd_category": "容器编排/K8s辅助工具",
  "cmd_dimension": "K8s辅助工具",
  "cmd_install": "kubectl krew install tree",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "k9s"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-utilities.yaml"
}
---

# kubectl-tree

> 以树状结构展示 K8s 资源 ownerReferences 关系

## 安装

```bash
kubectl krew install tree
```

## 用法

```
kubectl tree [OPTIONS] RESOURCE NAME
```

## 参数

| Flag | Description |
|------|-------------|
| `--all-namespaces` | 扫描所有命名空间 |

## 示例

### 示例 1: 查看 Deployment 下的所有派生资源

```bash
kubectl tree deployment myapp
```

### 示例 2: 查看 default 命名空间下的资源树

```bash
kubectl tree namespace default
```

## 关联命令

- [[kubectl]]
- [[k9s]]

## 风险提示

> ⚠️ **LOW**: 只读命令

## 所属维度

[[K8s辅助工具-MOC|容器编排/K8s辅助工具]]
