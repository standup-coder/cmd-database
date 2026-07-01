---
{
  "cmd_name": "buildah",
  "cmd_category": "容器编排/容器替代方案",
  "cmd_dimension": "容器替代方案",
  "cmd_install": "参考 https://github.com/containers/buildah/blob/main/install.md",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "podman",
    "skopeo"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/docker/container-alternatives.yaml"
}
---

# buildah

> 构建 OCI 容器镜像，无需完整容器运行时

## 安装

```bash
参考 https://github.com/containers/buildah/blob/main/install.md
```

## 用法

```
buildah [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `bud` | 使用 Dockerfile 构建镜像 |
| `from` | 从基础镜像创建工作容器 |
| `commit` | 将工作容器保存为镜像 |

## 示例

### 示例 1: 使用 Dockerfile 构建镜像

```bash
buildah bud -t myapp .
```

### 示例 2: 从 alpine 创建构建容器

```bash
buildah from alpine:latest
```

## 关联命令

- [[podman]]
- [[skopeo]]

## 风险提示

> ⚠️ **LOW**: 构建时避免在镜像层中遗留密钥等敏感文件

## 所属维度

[[容器替代方案-MOC|容器编排/容器替代方案]]
