---
{
  "cmd_name": "docker buildx",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "Docker Desktop 自带或 docker-buildx 插件",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker build",
    "buildkit"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# docker buildx

> Docker 高级镜像构建插件

## 安装

```bash
Docker Desktop 自带或 docker-buildx 插件
```

## 用法

```
docker buildx [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `build` | 构建 |
| `create` | 创建 builder |
| `ls` | 列出 builder |
| `bake` | 批量构建 |

## 示例

### 示例 1: 多平台构建

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t myapp .
```

### 示例 2: 列出 builders

```bash
docker buildx ls
```

## 关联命令

- [[docker-build]]
- [[buildkit]]

## 风险提示

> ⚠️ **MEDIUM**: 多平台构建和缓存导出可能产生大量临时文件

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
