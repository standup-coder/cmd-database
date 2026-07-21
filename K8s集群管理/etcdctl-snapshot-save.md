---
{
  "cmd_name": "etcdctl snapshot save",
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

# etcdctl snapshot save

> Create backup snapshot of etcd data

## 安装

```bash
Installed with etcd or download from etcd releases
```

## 用法

```
etcdctl snapshot save [snapshot-file]
```

## 参数

| Flag | Description |
|------|-------------|
| `--endpoints` | Comma-separated list of etcd endpoints |
| `--cacert` | Path to CA certificate |
| `--cert` | Path to client certificate |
| `--key` | Path to client key |

## 示例

### 示例 1: Save etcd snapshot to file

```bash
etcdctl snapshot save /backup/etcd-snapshot.db
```

### 示例 2: Save snapshot with TLS authentication

```bash
etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /backup/snapshot.db
```

## 风险提示

> ⚠️ **LOW**: Read-only backup operation; safe to perform

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
