---
{
  "cmd_name": "linkerd",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://linkerd.io/2/getting-started/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "istioctl",
    "kubectl"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# linkerd

> 轻量级 Service Mesh CLI

## 安装

```bash
参考 https://linkerd.io/2/getting-started/
```

## 用法

```
linkerd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `check` | 检查集群 |
| `install` | 安装控制平面 |
| `inject` | 自动注入 sidecar |
| `stat` | 查看统计 |

## 示例

### 示例 1: 检查 Linkerd 安装

```bash
linkerd check
```

### 示例 2: 注入 sidecar 并部署

```bash
linkerd inject deploy.yml | kubectl apply -f -
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 控制平面变更会影响流量治理，请在维护窗口执行

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
