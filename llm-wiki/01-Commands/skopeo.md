---
{
  "cmd_name": "skopeo",
  "cmd_category": "容器编排/容器替代方案",
  "cmd_dimension": "容器替代方案",
  "cmd_install": "包管理器安装，如 sudo apt install skopeo / sudo yum install skopeo",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker",
    "podman"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/docker/container-alternatives.yaml"
}
---

# skopeo

> 容器镜像仓库操作工具，支持复制、检查签名

## 安装

```bash
包管理器安装，如 sudo apt install skopeo / sudo yum install skopeo
```

## 用法

```
skopeo [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `inspect` | 查看远程镜像元数据 |
| `copy` | 在不同仓库之间复制镜像 |
| `sync` | 同步镜像仓库 |

## 示例

### 示例 1: 查看远程镜像信息

```bash
skopeo inspect docker://registry.example.com/myapp:latest
```

### 示例 2: 复制镜像到另一个仓库

```bash
skopeo copy docker://src/myapp:latest docker://dst/myapp:latest
```

## 关联命令

- [[podman]]

## 风险提示

> ⚠️ **MEDIUM**: 复制镜像会覆盖目标 tag，请确认源和目标地址

## 所属维度

[[容器替代方案-MOC|容器编排/容器替代方案]]
