---
{
  "cmd_name": "lxd",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://documentation.ubuntu.com/lxd/en/latest/installing/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lxc",
    "incus"
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

# lxd

> LXC 系统容器管理守护进程

## 安装

```bash
参考 https://documentation.ubuntu.com/lxd/en/latest/installing/
```

## 用法

```
lxd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化 |
| `list` |  |
| `launch` |  |
| `exec` |  |

## 示例

### 示例 1: 初始化 LXD

```bash
lxd init
```

### 示例 2: 列出 LXD 容器

```bash
lxc list
```

## 关联命令

- [[lxc]]
- [[incus]]

## 风险提示

> ⚠️ **MEDIUM**: LXD 是系统级服务，请正确配置存储和网络

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
