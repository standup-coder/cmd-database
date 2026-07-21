---
{
  "cmd_name": "docker volume",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "docker run",
    "docker network"
  ],
  "cmd_tags": [
    "docker",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/container/cloudnative/cloudnative-extra.yaml"
}
---

# docker volume

> Docker 卷管理

## 用法

```
docker volume [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建卷 |
| `ls` | 列出 |
| `inspect` | 查看 |
| `rm` | 删除 |

## 示例

### 示例 1: 创建命名卷

```bash
docker volume create myvol
```

### 示例 2: 删除卷

```bash
docker volume rm myvol
```

## 关联命令

- [[docker-run]]
- [[docker-network]]

## 风险提示

> ⚠️ **HIGH**: 删除卷会丢失持久化数据，请确认无容器使用

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
