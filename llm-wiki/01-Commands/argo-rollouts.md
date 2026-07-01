---
{
  "cmd_name": "argo-rollouts",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "kubectl krew install argo-rollouts",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "argocd",
    "flagger"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# argo-rollouts

> Argo Rollouts 渐进式交付 CLI

## 安装

```bash
kubectl krew install argo-rollouts
```

## 用法

```
argo-rollouts [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `list` |  |
| `get` |  |
| `promote` |  |
| `abort` |  |
| `restart` |  |

## 示例

### 示例 1: 列出 Rollouts

```bash
kubectl argo rollouts list rollouts
```

### 示例 2: 推进 rollout

```bash
kubectl argo rollouts promote my-rollout
```

## 关联命令

- [[flagger]]

## 风险提示

> ⚠️ **HIGH**: promote/abort 会改变生产流量分布，请确认指标健康

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
