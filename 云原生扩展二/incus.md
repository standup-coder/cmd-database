---
{
  "cmd_name": "incus",
  "cmd_category": "容器编排/云原生扩展二",
  "cmd_dimension": "云原生扩展二",
  "cmd_install": "参考 https://linuxcontainers.org/incus/docs/main/installing/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lxd",
    "lxc"
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

# incus

> LXD 社区分支（Canonical 替代方案）

## 安装

```bash
参考 https://linuxcontainers.org/incus/docs/main/installing/
```

## 用法

```
incus [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `admin` | init |
| `list` |  |
| `launch` |  |
| `exec` |  |

## 示例

### 示例 1: 初始化 Incus

```bash
incus admin init
```

### 示例 2: 创建容器

```bash
incus launch images:ubuntu/22.04 c1
```

## 关联命令

- [[lxd]]
- [[lxc]]

## 风险提示

> ⚠️ **MEDIUM**: 同 LXD，需注意存储和网络配置

## 所属维度

[[云原生扩展二-MOC|容器编排/云原生扩展二]]
