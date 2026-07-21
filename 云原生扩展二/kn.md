---
{
  "cmd_name": "kn",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://knative.dev/docs/client/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "istio"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# kn

> Knative 命令行工具

## 安装

```bash
参考 https://knative.dev/docs/client/install/
```

## 用法

```
kn [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `service` | 管理服务 |
| `revision` |  |
| `route` |  |
| `plugin` |  |

## 示例

### 示例 1: 创建 Knative 服务

```bash
kn service create hello --image gcr.io/knative-samples/helloworld-go
```

### 示例 2: 列出服务

```bash
kn service list
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: kn service delete 会删除 Serverless 服务，请确认

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
