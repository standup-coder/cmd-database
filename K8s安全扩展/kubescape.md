---
{
  "cmd_name": "kubescape",
  "cmd_category": "容器编排/K8s安全扩展",
  "cmd_dimension": "K8s安全扩展",
  "cmd_install": "参考 https://github.com/kubescape/kubescape/releases",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kube-bench",
    "trivy"
  ],
  "cmd_tags": [
    "safety",
    "kubernetes",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/k8s/k8s-security-extra.yaml"
}
---

# kubescape

> Kubernetes 安全与合规扫描工具

## 安装

```bash
参考 https://github.com/kubescape/kubescape/releases
```

## 用法

```
kubescape [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `scan` | 扫描集群或 YAML |
| `framework` | 指定合规框架（如 nsa、mitre） |

## 示例

### 示例 1: 使用 NSA 框架扫描集群

```bash
kubescape scan framework nsa
```

### 示例 2: 扫描本地 YAML 清单

```bash
kubescape scan *.yaml
```

## 风险提示

> ⚠️ **LOW**: 扫描为只读操作，但会访问 K8s API，请使用最小权限 ServiceAccount

## 所属维度

[[K8s安全扩展-MOC|容器编排/K8s安全扩展]]
