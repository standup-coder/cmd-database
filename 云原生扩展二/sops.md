---
{
  "cmd_name": "sops",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/getsops/sops/releases",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "kubeseal",
    "gpg"
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

# sops

> 文件加密编辑器（支持 AWS/GCP/Azure/KMS）

## 安装

```bash
参考 https://github.com/getsops/sops/releases
```

## 用法

```
sops [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 加密 |
| `-d` | 解密 |
| `--kms` |  |
| `--pgp` |  |

## 示例

### 示例 1: 原地加密

```bash
sops -e -i secret.yaml
```

### 示例 2: 解密查看

```bash
sops -d secret.yaml
```

## 关联命令

- [[kubeseal]]

## 风险提示

> ⚠️ **HIGH**: 加密后丢失 KMS/PGP 密钥将无法解密，请妥善保存

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
