---
{
  "cmd_name": "lxc",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "包管理器安装，如 sudo apt install lxc",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lxd",
    "docker"
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

# lxc

> Linux 容器（LXC）管理

## 安装

```bash
包管理器安装，如 sudo apt install lxc
```

## 用法

```
lxc [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `launch` | 创建 |
| `list` | 列出 |
| `exec` | 执行 |
| `stop` | 停止 |

## 示例

### 示例 1: 创建容器

```bash
lxc launch ubuntu:22.04 mycontainer
```

### 示例 2: 进入容器

```bash
lxc exec mycontainer -- bash
```

## 关联命令

- [[lxd]]

## 风险提示

> ⚠️ **MEDIUM**: 特权容器可能逃逸，请限制权限

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
