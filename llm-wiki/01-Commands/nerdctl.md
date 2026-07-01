---
{
  "cmd_name": "nerdctl",
  "cmd_category": "容器编排/容器替代方案",
  "cmd_dimension": "容器替代方案",
  "cmd_install": "参考 https://github.com/containerd/nerdctl/blob/main/docs/install.md",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ctr",
    "crictl"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/docker/container-alternatives.yaml"
}
---

# nerdctl

> containerd 的 Docker 兼容 CLI

## 安装

```bash
参考 https://github.com/containerd/nerdctl/blob/main/docs/install.md
```

## 用法

```
nerdctl [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行容器 |
| `ps` | 列出容器 |
| `images` | 列出镜像 |

## 示例

### 示例 1: 在 containerd 上运行容器

```bash
nerdctl run -d --name nginx nginx:alpine
```

### 示例 2: 列出本地镜像

```bash
nerdctl images
```

## 关联命令

- [[ctr]]
- [[crictl]]

## 风险提示

> ⚠️ **MEDIUM**: nerdctl 直接操作 containerd，可能影响 Kubernetes 使用的容器

## 所属维度

[[容器替代方案-MOC|容器编排/容器替代方案]]
