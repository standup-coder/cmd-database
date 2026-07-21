---
{
  "cmd_name": "krew",
  "cmd_category": "容器编排/K8s开发工具",
  "cmd_dimension": "K8s开发工具",
  "cmd_install": "参考 https://krew.sigs.k8s.io/docs/user-guide/setup/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "kubectx"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-devtools.yaml"
}
---

# krew

> kubectl 插件包管理器

## 安装

```bash
参考 https://krew.sigs.k8s.io/docs/user-guide/setup/install/
```

## 用法

```
kubectl krew [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装插件 |
| `list` | 列出已安装插件 |
| `search` | 搜索插件 |

## 示例

### 示例 1: 安装 kubectx 插件

```bash
kubectl krew install ctx
```

### 示例 2: 搜索可用插件

```bash
kubectl krew search
```

## 关联命令

- [[kubectl]]
- [[kubectx]]

## 风险提示

> ⚠️ **MEDIUM**: 插件来自社区，请审查来源和权限后再安装

## 所属维度

[[K8s开发工具-MOC|容器编排/K8s开发工具]]
