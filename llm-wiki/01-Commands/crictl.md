---
{
  "cmd_name": "crictl",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "kubectl",
    "ctr"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-more.yaml"
}
---

# crictl

> 兼容 CRI 的容器运行时 CLI

## 安装

```bash
参考 https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md
```

## 用法

```
crictl [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `pods` |  |
| `ps` |  |
| `images` |  |
| `logs` |  |
| `exec` |  |

## 示例

### 示例 1: 列出 Pod

```bash
crictl pods
```

### 示例 2: 查看容器日志

```bash
crictl logs <container-id>
```

## 关联命令

- [[kubectl]]
- [[ctr]]

## 风险提示

> ⚠️ **MEDIUM**: crictl 可直接删除运行中容器，生产环境请谨慎

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
