---
cmd_name: journalctl -u kubelet
cmd_category: "容器编排/K8s集群管理"
cmd_dimension: Kubernetes Cluster Management
cmd_install: Built-in systemd command
cmd_platforms:
- linux
summary: "View kubelet service logs"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/k8s-cluster.yaml
---


# journalctl -u kubelet

> View kubelet service logs

## 安装

```bash
Built-in systemd command
```

## 用法

```
journalctl -u kubelet [flags]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | Follow log output in real-time |
| `-n` | Number of recent log entries to show |
| `--since` | Show logs since specific time |

## 示例

### 示例 1: Follow kubelet logs in real-time

```bash
journalctl -u kubelet -f
```

### 示例 2: Show last 100 log entries

```bash
journalctl -u kubelet -n 100
```

### 示例 3: Show logs from last 10 minutes

```bash
journalctl -u kubelet --since '10 minutes ago'
```

## 风险提示

> ⚠️ **LOW**: Read-only operation; views logs only

## 所属维度

[[K8s集群管理-MOC|Kubernetes Cluster Management]]
