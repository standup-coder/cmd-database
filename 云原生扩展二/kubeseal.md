---
{
  "cmd_name": "kubeseal",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/bitnami-labs/sealed-secrets/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "sops"
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

# kubeseal

> Sealed Secrets 加密 CLI

## 安装

```bash
参考 https://github.com/bitnami-labs/sealed-secrets/releases
```

## 用法

```
kubeseal [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--format` | yaml\|json |
| `--scope` |  |
| `--cert` |  |

## 示例

### 示例 1: 加密 Secret

```bash
kubeseal < secret.yaml > sealedsecret.yaml
```

### 示例 2: 获取公钥

```bash
kubeseal --controller-namespace=kube-system --fetch-cert > cert.pem
```

## 关联命令

- [[kubectl]]
- [[sops]]

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
