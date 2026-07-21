---
{
  "cmd_name": "containerd",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://github.com/containerd/containerd/blob/main/docs/getting-started.md",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "ctr",
    "nerdctl"
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

# containerd

> 容器运行时 daemon

## 安装

```bash
参考 https://github.com/containerd/containerd/blob/main/docs/getting-started.md
```

## 用法

```
containerd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--config` | 配置文件 |
| `--log-level` |  |

## 示例

### 示例 1: 启动 containerd

```bash
sudo containerd
```

### 示例 2: 指定配置启动

```bash
sudo containerd -c /etc/containerd/config.toml
```

## 关联命令

- [[ctr]]
- [[nerdctl]]

## 风险提示

> ⚠️ **MEDIUM**: containerd 是底层运行时，配置错误会导致容器无法启动

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
