---
{
  "cmd_name": "crossplane",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://docs.crossplane.io/latest/software/install/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "terraform"
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

# crossplane

> Kubernetes 多云控制平面 CLI

## 安装

```bash
参考 https://docs.crossplane.io/latest/software/install/
```

## 用法

```
crossplane [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `xpkg` | 管理包 |
| `trace` | 追踪资源 |
| `beta` |  |

## 示例

### 示例 1: 安装 AWS provider

```bash
crossplane xpkg install provider crossplane/provider-aws
```

### 示例 2: 追踪资源状态

```bash
crossplane trace resource mydb -n default
```

## 关联命令

- [[kubectl]]
- [[terraform]]

## 风险提示

> ⚠️ **MEDIUM**: Managed Resources 会创建真实云资源，请确认 provider 配置

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
