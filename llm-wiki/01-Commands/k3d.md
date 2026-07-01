---
{
  "cmd_name": "k3d",
  "cmd_category": "容器编排/本地K8s",
  "cmd_dimension": "本地K8s",
  "cmd_install": "参考 https://k3d.io/v5.0.0/#installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "kind"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/local-k8s.yaml"
}
---

# k3d

> 在 Docker 中运行 k3s 集群

## 安装

```bash
参考 https://k3d.io/v5.0.0/#installation
```

## 用法

```
k3d [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `cluster create` | 创建 k3s 集群 |
| `cluster delete` | 删除 k3s 集群 |
| `image import` | 导入镜像到集群 |

## 示例

### 示例 1: 创建本地 k3s 集群

```bash
k3d cluster create mycluster
```

### 示例 2: 导入本地镜像到 k3d 集群

```bash
k3d image import myapp:latest -c mycluster
```

## 关联命令

- [[kubectl]]
- [[kind]]

## 风险提示

> ⚠️ **MEDIUM**: 多个本地集群会占用大量资源，请及时清理不再使用的集群

## 所属维度

[[本地K8s-MOC|容器编排/本地K8s]]
