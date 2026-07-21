---
{
  "cmd_name": "kaniko",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://github.com/GoogleContainerTools/kaniko",
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

# kaniko

> 无需特权 Docker daemon 的镜像构建工具

## 安装

```bash
参考 https://github.com/GoogleContainerTools/kaniko
```

## 用法

```
kaniko [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--dockerfile` | Dockerfile |
| `--context` |  |
| `--destination` |  |
| `--no-push` |  |

## 示例

### 示例 1: 构建并推送镜像

```bash
executor --dockerfile Dockerfile --context . --destination registry/myapp:v1
```

### 示例 2: 只构建不推送

```bash
executor --dockerfile Dockerfile --context . --no-push
```

## 关联命令

- [[docker-build]]
- [[buildkit]]

## 风险提示

> ⚠️ **MEDIUM**: kaniko 会访问 registry 凭据，请确保 Secret 安全

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
