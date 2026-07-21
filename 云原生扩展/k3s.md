---
{
  "cmd_name": "k3s",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://docs.k3s.io/quick-start",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "kind"
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

# k3s

> 轻量级 Kubernetes 发行版

## 安装

```bash
参考 https://docs.k3s.io/quick-start
```

## 用法

```
k3s [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `server` | 启动 server |
| `agent` | 启动 agent |
| `kubectl` | 子命令 |

## 示例

### 示例 1: 安装并启动 k3s

```bash
curl -sfL https://get.k3s.io | sh -
```

### 示例 2: 使用 k3s 内置 kubectl

```bash
k3s kubectl get nodes
```

## 关联命令

- [[kubectl]]
- [[kind]]

## 风险提示

> ⚠️ **MEDIUM**: k3s 会修改系统配置并启动容器，请确认环境隔离

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
