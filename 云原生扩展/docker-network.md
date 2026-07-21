---
{
  "cmd_name": "docker network",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker run",
    "docker volume"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# docker network

> Docker 网络管理

## 用法

```
docker network [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建网络 |
| `ls` | 列出 |
| `inspect` | 查看 |
| `rm` | 删除 |

## 示例

### 示例 1: 创建桥接网络

```bash
docker network create mynet
```

### 示例 2: 连接容器到网络

```bash
docker network connect mynet mycontainer
```

## 关联命令

- [[docker-run]]
- [[docker-volume]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
