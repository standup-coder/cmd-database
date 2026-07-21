---
{
  "cmd_name": "docker rm",
  "cmd_category": "容器编排/Docker命令",
  "cmd_dimension": "Docker命令",
  "cmd_install": "参考 https://docs.docker.com/engine/install/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "docker rmi",
    "docker ps"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/container/docker/docker.yaml"
}
---

# docker rm

> 删除容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f, --force` | 强制删除运行中的容器 |
| `-v` | 删除关联的卷 |

## 示例

### 示例 1: 删除已停止的容器

```bash
docker rm my-container
```

### 示例 2: 强制删除容器

```bash
docker rm -f my-container
```

## 关联命令

- [[docker-rmi]]
- [[docker-ps]]

## 风险提示

> ⚠️ **MEDIUM**: 删除容器会丢失容器内的数据(除非使用卷)

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
