---
{
  "cmd_name": "clusterctl",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://cluster-api.sigs.k8s.io/clusterctl/overview.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "kubeadm"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# clusterctl

> Cluster API 集群生命周期管理

## 安装

```bash
参考 https://cluster-api.sigs.k8s.io/clusterctl/overview.html
```

## 用法

```
clusterctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化管理集群 |
| `generate` | cluster 生成集群 YAML |
| `move` | 迁移集群 |

## 示例

### 示例 1: 初始化 AWS provider

```bash
clusterctl init --infrastructure aws
```

### 示例 2: 生成工作负载集群清单

```bash
clusterctl generate cluster my-cluster --kubernetes-version v1.28.0 > cluster.yaml
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **HIGH**: clusterctl 管理 Kubernetes 集群生命周期，误操作可能影响管理平面

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
