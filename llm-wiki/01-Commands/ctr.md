---
{
  "cmd_name": "ctr",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "随 containerd 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nerdctl",
    "crictl"
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

# ctr

> containerd 官方 CLI

## 安装

```bash
随 containerd 安装
```

## 用法

```
ctr [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `images` | 镜像 |
| `containers` | 容器 |
| `run` | 运行 |
| `pull` | 拉取 |

## 示例

### 示例 1: 列出镜像

```bash
ctr images ls
```

### 示例 2: 运行容器

```bash
ctr run docker.io/library/nginx:latest nginx
```

## 关联命令

- [[nerdctl]]
- [[crictl]]

## 风险提示

> ⚠️ **MEDIUM**: ctr 直接操作 containerd，可能影响 Kubernetes 容器

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
