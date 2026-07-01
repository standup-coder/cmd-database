---
{
  "cmd_name": "dapr",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://docs.dapr.io/getting-started/install-dapr-cli/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubectl",
    "service-mesh"
  ],
  "cmd_tags": [
    "application",
    "distributed",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# dapr

> 分布式应用运行时 CLI

## 安装

```bash
参考 https://docs.dapr.io/getting-started/install-dapr-cli/
```

## 用法

```
dapr [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化 |
| `run` | 运行 |
| `publish` |  |
| `invoke` |  |

## 示例

### 示例 1: 初始化 Dapr

```bash
dapr init
```

### 示例 2: 带 Dapr sidecar 运行应用

```bash
dapr run --app-id myapp --app-port 8080 -- python app.py
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: dapr init 会部署控制平面，请确认 Kubernetes 上下文

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
