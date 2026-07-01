---
{
  "cmd_name": "kustomize",
  "cmd_category": "容器编排/K8s开发工具",
  "cmd_dimension": "K8s开发工具",
  "cmd_install": "参考 https://kubectl.docs.kubernetes.io/installation/kustomize/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "helm"
  ],
  "cmd_tags": [
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-devtools.yaml"
}
---

# kustomize

> Kubernetes 声明式配置自定义工具

## 安装

```bash
参考 https://kubectl.docs.kubernetes.io/installation/kustomize/
```

## 用法

```
kustomize [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `build` | 根据 kustomization.yaml 构建完整 YAML |
| `edit` | 编辑 kustomization 配置 |

## 示例

### 示例 1: 构建生产环境覆盖后的 K8s 清单

```bash
kustomize build ./overlays/production
```

### 示例 2: 修改 kustomization 中的镜像标签

```bash
kustomize edit set image myapp=myapp:v2.0
```

## 关联命令

- [[kubectl]]

## 风险提示

> ⚠️ **LOW**: kustomize build 为本地渲染，不会直接修改集群

## 所属维度

[[K8s开发工具-MOC|容器编排/K8s开发工具]]
