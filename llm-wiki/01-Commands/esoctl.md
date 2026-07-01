---
{
  "cmd_name": "esoctl",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "kubectl krew install external-secrets",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubeseal",
    "vault"
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

# esoctl

> External Secrets Operator 工具（kubectl 插件）

## 安装

```bash
kubectl krew install external-secrets
```

## 用法

```
esoctl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `get` | secrets |
| `get` | secretstores |
| `validate` |  |

## 示例

### 示例 1: 列出外部同步的 Secret

```bash
kubectl externalsecrets get secrets
```

### 示例 2: 列出 SecretStore

```bash
kubectl externalsecrets get secretstores
```

## 关联命令

- [[kubeseal]]
- [[vault]]

## 风险提示

> ⚠️ **MEDIUM**: 错误的 SecretStore 会同步错误凭据，请确认 provider 配置

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
