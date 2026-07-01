---
{
  "cmd_name": "microk8s",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "sudo snap install microk8s --classic",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "k3s"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# microk8s

> Ubuntu 官方轻量 Kubernetes 发行版

## 安装

```bash
sudo snap install microk8s --classic
```

## 用法

```
microk8s [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `status` | 查看状态 |
| `enable` | 启用插件 |
| `kubectl` | 子命令 |

## 示例

### 示例 1: 查看 MicroK8s 状态

```bash
microk8s status
```

### 示例 2: 启用 dns 和 ingress 插件

```bash
microk8s enable dns ingress
```

## 关联命令

- [[kubectl]]
- [[k3s]]

## 风险提示

> ⚠️ **MEDIUM**: snap 安装会修改系统，生产环境请先评估

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
