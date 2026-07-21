---
{
  "cmd_name": "docker system",
  "cmd_category": "容器编排/云原生扩展",
  "cmd_dimension": "云原生扩展",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "docker",
    "docker volume"
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

# docker system

> Docker 系统级维护命令

## 用法

```
docker system [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `df` | 查看磁盘使用 |
| `prune` | 清理未使用数据 |
| `info` | 系统信息 |

## 示例

### 示例 1: 查看 Docker 磁盘使用

```bash
docker system df
```

### 示例 2: 清理所有未使用镜像和卷（谨慎）

```bash
docker system prune -a
```

## 关联命令

- [[docker-volume]]

## 风险提示

> ⚠️ **HIGH**: prune 会删除未使用的镜像、容器、网络和卷，请确认后再执行

## 所属维度

[[云原生扩展-MOC|容器编排/云原生扩展]]
