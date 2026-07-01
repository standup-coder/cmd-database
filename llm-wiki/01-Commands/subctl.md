---
{
  "cmd_name": "subctl",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://submariner.io/operations/deployment/subctl/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "cilium"
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

# subctl

> Submariner 跨集群网络 CLI

## 安装

```bash
参考 https://submariner.io/operations/deployment/subctl/
```

## 用法

```
subctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `deploy-broker` |  |
| `join` |  |
| `show` | connections |
| `verify` |  |

## 示例

### 示例 1: 部署 broker

```bash
subctl deploy-broker
```

### 示例 2: 加入集群

```bash
subctl join --kubeconfig cluster2.kubeconfig broker-info.subm
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **HIGH**: 跨集群网络会打通多个集群，请确认 CIDR 不冲突

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
