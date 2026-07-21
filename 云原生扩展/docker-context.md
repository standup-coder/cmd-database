---
{
  "cmd_name": "docker context",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker",
    "kubectl config"
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

# docker context

> Docker 上下文管理

## 用法

```
docker context [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `create` | 创建上下文 |
| `use` | 切换上下文 |
| `ls` | 列出 |
| `rm` | 删除 |

## 示例

### 示例 1: 列出上下文

```bash
docker context ls
```

### 示例 2: 创建远程上下文

```bash
docker context create remote --docker host=ssh://user@host
```

## 关联命令

- [[kubectl config]]

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
