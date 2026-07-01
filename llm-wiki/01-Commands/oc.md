---
{
  "cmd_name": "oc",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "helm"
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

# oc

> OpenShift 命令行工具

## 安装

```bash
参考 https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html
```

## 用法

```
oc [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `login` | 登录 |
| `new-project` | 创建项目 |
| `adm` | 管理命令 |

## 示例

### 示例 1: 登录 OpenShift

```bash
oc login https://api.example.com:6443
```

### 示例 2: 创建新项目

```bash
oc new-project myproject
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **MEDIUM**: oc 拥有 cluster-admin 能力时请谨慎使用

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
