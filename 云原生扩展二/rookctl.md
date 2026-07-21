---
{
  "cmd_name": "rookctl",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "Rook 使用 kubectl 与 CRD 管理，无独立 CLI，可用 kubectl rook-ceph 插件",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "longhornctl"
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

# rookctl

> Rook Ceph 存储管理

## 安装

```bash
Rook 使用 kubectl 与 CRD 管理，无独立 CLI，可用 kubectl rook-ceph 插件
```

## 用法

```
rookctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `mon` |  |
| `osd` |  |
| `status` |  |

## 示例

### 示例 1: 查看 Ceph 健康

```bash
kubectl rook-ceph health
```

### 示例 2: 执行 ceph status

```bash
kubectl rook-ceph ceph status
```

## 关联命令

- [[kubectl]]
- [[longhornctl]]

## 风险提示

> ⚠️ **HIGH**: 直接操作 Ceph 集群会影响存储，请确认命令影响

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
