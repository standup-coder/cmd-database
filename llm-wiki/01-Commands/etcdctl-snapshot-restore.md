---
{
  "cmd_name": "etcdctl snapshot restore",
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
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-cluster.yaml"
}
---

# etcdctl snapshot restore

> Restore etcd cluster from backup snapshot

## 安装

```bash
Installed with etcd or download from etcd releases
```

## 用法

```
etcdctl snapshot restore [snapshot-file] [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `--data-dir` | Path to restore data directory |
| `--name` | Human-readable name for etcd member |
| `--initial-cluster` | Initial cluster configuration |
| `--initial-cluster-token` | Initial cluster token for the etcd cluster during restore |
| `--initial-advertise-peer-urls` | List of this member's peer URLs |

## 示例

### 示例 1: Restore snapshot to new data directory

```bash
etcdctl snapshot restore /backup/snapshot.db --data-dir=/var/lib/etcd-restore
```

### 示例 2: Restore with full cluster configuration

```bash
etcdctl snapshot restore snapshot.db --name=node1 --initial-cluster=node1=http://10.0.0.1:2380 --initial-advertise-peer-urls=http://10.0.0.1:2380 --data-dir=/var/lib/etcd
```

## 风险提示

> ⚠️ **CRITICAL**: Restoring snapshot replaces current cluster data; backup first

## 所属维度

[[Kubernetes Cluster Management-MOC|Kubernetes Cluster Management]]
