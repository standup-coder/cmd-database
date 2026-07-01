---
{
  "cmd_name": "cert-manager",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://cert-manager.io/docs/reference/cmctl/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "openssl"
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

# cert-manager

> Kubernetes 证书自动化管理（cmctl）

## 安装

```bash
参考 https://cert-manager.io/docs/reference/cmctl/
```

## 用法

```
cert-manager [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `check` | 检查 |
| `status` | 查看证书状态 |
| `renew` | 手动续期 |

## 示例

### 示例 1: 检查 cert-manager API

```bash
cmctl check api
```

### 示例 2: 查看证书状态

```bash
cmctl status certificate mycert -n default
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: 手动 renew 或删除证书可能导致服务 TLS 中断

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
