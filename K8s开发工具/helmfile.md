---
{
  "cmd_name": "helmfile",
  "cmd_category": "容器编排/K8s开发工具",
  "cmd_dimension": "K8s开发工具",
  "cmd_install": "参考 https://helmfile.readthedocs.io/en/latest/#installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "helm",
    "kubectl"
  ],
  "cmd_tags": [
    "deployment",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-devtools.yaml"
}
---

# helmfile

> Helm Chart 的声明式批量部署工具

## 安装

```bash
参考 https://helmfile.readthedocs.io/en/latest/#installation
```

## 用法

```
helmfile [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `apply` | 根据 helmfile.yaml 同步 release |
| `sync` | 同步所有 release |
| `destroy` | 删除 helmfile 中定义的所有 release |

## 示例

### 示例 1: 应用 helmfile 配置

```bash
helmfile apply
```

### 示例 2: 同步指定环境 helmfile

```bash
helmfile -f helmfile.d/prod.yaml sync
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **HIGH**: destroy 会删除所有定义 release，请确认环境与影响范围

## 所属维度

[[K8s开发工具-MOC|容器编排/K8s开发工具]]
