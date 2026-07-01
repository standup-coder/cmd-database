---
{
  "cmd_name": "podman",
  "cmd_category": "容器编排/容器替代方案",
  "cmd_dimension": "容器替代方案",
  "cmd_install": "参考 https://podman.io/docs/installation",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker",
    "buildah"
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

# podman

> 无守护进程的容器引擎，兼容 Docker CLI

## 安装

```bash
参考 https://podman.io/docs/installation
```

## 用法

```
podman [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `run` | 运行容器 |
| `ps` | 列出容器 |
| `build` | 构建镜像 |

## 示例

### 示例 1: 后台运行 nginx 容器

```bash
podman run -d -p 8080:80 nginx
```

### 示例 2: 使用当前目录 Dockerfile 构建镜像

```bash
podman build -t myapp .
```

## 关联命令

- [[buildah]]

## 风险提示

> ⚠️ **MEDIUM**: rootless 模式虽好，但仍需注意镜像来源和端口暴露范围

## 所属维度

[[容器替代方案-MOC|容器编排/容器替代方案]]
