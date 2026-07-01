---
{
  "cmd_name": "hubble",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://docs.cilium.io/en/stable/gettingstarted/hubble_setup/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cilium",
    "kubectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# hubble

> Cilium 可观测性 CLI

## 安装

```bash
参考 https://docs.cilium.io/en/stable/gettingstarted/hubble_setup/
```

## 用法

```
hubble [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `observe` | 观察流 |
| `status` | 状态 |
| `list` | nodes |

## 示例

### 示例 1: 观察网络流

```bash
hubble observe
```

### 示例 2: 观察指定 Pod 流

```bash
hubble observe --pod default/myapp
```

## 关联命令

- [[kubectl]]

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
