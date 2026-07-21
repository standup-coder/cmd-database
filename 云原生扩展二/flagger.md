---
{
  "cmd_name": "flagger",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://flagger.app/install/flagger-install-on-kubernetes/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "argocd",
    "argo-rollouts"
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

# flagger

> Flagger 渐进式交付控制器

## 安装

```bash
参考 https://flagger.app/install/flagger-install-on-kubernetes/
```

## 用法

```
flagger [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `loadtester` |  |
| `generate` |  |

## 示例

### 示例 1: 安装 Flagger

```bash
kubectl apply -k github.com/fluxcd/flagger//kustomize/base
```

### 示例 2: 生成示例 canary

```bash
flagger generate -n test
```

## 关联命令

- [[argo-rollouts]]

## 风险提示

> ⚠️ **HIGH**: Canary 发布会影响生产流量，请配置正确阈值

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
