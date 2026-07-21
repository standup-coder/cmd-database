---
{
  "cmd_name": "vault",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://developer.hashicorp.com/vault/downloads",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "consul",
    "kubectl"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# vault

> HashiCorp Vault 密钥管理 CLI

## 安装

```bash
参考 https://developer.hashicorp.com/vault/downloads
```

## 用法

```
vault [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `kv` | 管理键值对 |
| `auth` | 管理认证 |
| `policy` | 管理策略 |
| `status` |  |

## 示例

### 示例 1: 查看 Vault 状态

```bash
vault status
```

### 示例 2: 读取密钥

```bash
vault kv get secret/myapp
```

## 关联命令

- [[consul]]
- [[kubectl]]

## 风险提示

> ⚠️ **CRITICAL**: Vault 管理敏感凭据，错误策略或 root token 泄露会造成严重安全事故

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
