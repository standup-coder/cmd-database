---
{
  "cmd_name": "buildkit",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://github.com/moby/buildkit/blob/master/README.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker buildx",
    "kaniko"
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

# buildkit

> Docker/Moby 下一代镜像构建工具包

## 安装

```bash
参考 https://github.com/moby/buildkit/blob/master/README.md
```

## 用法

```
buildkit [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `buildctl` | 命令行 |
| `--addr` | 指定 buildkitd 地址 |

## 示例

### 示例 1: 使用 Dockerfile 构建

```bash
buildctl build --frontend dockerfile.v0 --local context=. --local dockerfile=.
```

### 示例 2: 查看磁盘使用

```bash
buildctl du
```

## 关联命令

- [[docker-buildx]]
- [[kaniko]]

## 风险提示

> ⚠️ **MEDIUM**: 构建会执行 Dockerfile 中的指令，请审查基础镜像和命令

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
