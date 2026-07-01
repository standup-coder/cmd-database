---
{
  "cmd_name": "img",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "参考 https://github.com/genuinetools/img",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "buildkit",
    "docker"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# img

> 由 buildkit 支持的无 daemon 镜像构建工具

## 安装

```bash
参考 https://github.com/genuinetools/img
```

## 用法

```
img [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `build` | 构建 |
| `tag` | 标签 |
| `push` | 推送 |
| `pull` | 拉取 |

## 示例

### 示例 1: 构建镜像

```bash
img build -t myapp .
```

### 示例 2: 打标签

```bash
img tag myapp registry/myapp:v1
```

## 关联命令

- [[buildkit]]

## 风险提示

> ⚠️ **MEDIUM**: img 以非 root 运行但仍在用户命名空间，注意缓存目录权限

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
