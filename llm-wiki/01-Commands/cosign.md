---
{
  "cmd_name": "cosign",
  "cmd_category": "容器编排/K8s安全扩展",
  "cmd_dimension": "K8s安全扩展",
  "cmd_install": "参考 https://docs.sigstore.dev/cosign/installation/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "skopeo",
    "trivy"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security-extra.yaml"
}
---

# cosign

> 容器镜像签名与验证工具

## 安装

```bash
参考 https://docs.sigstore.dev/cosign/installation/
```

## 用法

```
cosign [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `sign` | 对镜像进行签名 |
| `verify` | 验证镜像签名 |
| `generate-key-pair` | 生成密钥对 |

## 示例

### 示例 1: 生成签名密钥对

```bash
cosign generate-key-pair
```

### 示例 2: 验证镜像签名

```bash
cosign verify --key cosign.pub registry.example.com/myapp:v1
```

## 关联命令

- [[skopeo]]

## 风险提示

> ⚠️ **MEDIUM**: 私钥泄露会导致他人伪造签名，请使用 KMS 或安全存储

## 所属维度

[[K8s安全扩展-MOC|容器编排/K8s安全扩展]]
