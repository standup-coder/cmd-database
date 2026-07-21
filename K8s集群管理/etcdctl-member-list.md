---
{
  "cmd_name": "etcdctl member list",
  "cmd_category": "Kubernetes Cluster Management",
  "cmd_dimension": "Kubernetes Cluster Management",
  "cmd_install": "Installed with etcd or download from etcd releases",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# etcdctl member list

> List all etcd cluster members

## 安装

```bash
Installed with etcd or download from etcd releases
```

## 用法

```
etcdctl member list [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--endpoints` | Comma-separated list of etcd endpoints |
| `-w` | Output format: simple, json, table |

## 示例

### 示例 1: List cluster members in simple format

```bash
etcdctl member list
```

### 示例 2: List members in table format

```bash
etcdctl member list -w table
```

### 示例 3: List members with TLS authentication

```bash
etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key member list
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; lists members only

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
