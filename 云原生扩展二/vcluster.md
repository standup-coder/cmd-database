---
{
  "cmd_name": "vcluster",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://www.vcluster.com/docs/getting-started/install",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kind",
    "k3s"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# vcluster

> Kubernetes 虚拟集群

## 安装

```bash
参考 https://www.vcluster.com/docs/getting-started/install
```

## 用法

```
vcluster [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建 |
| `connect` | 连接 |
| `list` |  |
| `delete` |  |

## 示例

### 示例 1: 创建虚拟集群

```bash
vcluster create my-vcluster
```

### 示例 2: 连接虚拟集群

```bash
vcluster connect my-vcluster
```

## 关联命令

- [[kind]]
- [[k3s]]

## 风险提示

> ⚠️ **MEDIUM**: vcluster 共享宿主机集群资源，请注意配额和权限

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
