---
{
  "cmd_name": "etcdctl get",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "Installed with etcd or download from etcd releases",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# etcdctl get

> Get value of specified key from etcd

## 安装

```bash
Installed with etcd or download from etcd releases
```

## 用法

```
etcdctl get [key] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--prefix` | Get all keys with matching prefix |
| `--keys-only` | Get only keys, not values |
| `-w` | Output format: simple, json, fields |

## 示例

### 示例 1: List all pod keys in etcd

```bash
etcdctl get /registry/pods --prefix --keys-only
```

### 示例 2: Get specific namespace data

```bash
etcdctl get /registry/namespaces/default
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; retrieves data only

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
