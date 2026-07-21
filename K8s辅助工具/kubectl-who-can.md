---
{
  "cmd_name": "kubectl-who-can",
  "cmd_category": "容器编排/K8s辅助工具",
  "cmd_dimension": "K8s辅助工具",
  "cmd_install": "kubectl krew install who-can",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "krew"
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

# kubectl-who-can

> 检查谁对某个 K8s 资源拥有特定权限

## 安装

```bash
kubectl krew install who-can
```

## 用法

```
kubectl who-can VERB RESOURCE [NAME]
```

## 参数

| Flag | Description |
|------|-------------|
| `--all-namespaces` | 扫描所有命名空间 |

## 示例

### 示例 1: 查看谁能创建 Pod

```bash
kubectl who-can create pods
```

### 示例 2: 查看谁能删除 production 命名空间的 Secret

```bash
kubectl who-can delete secrets -n production
```

## 关联命令

- [[kubectl]]
- [[krew]]

## 风险提示

> ⚠️ **LOW**: 只读查询 RBAC 权限，不会修改集群

## 所属维度

[[K8s辅助工具-MOC|容器编排/K8s辅助工具]]
