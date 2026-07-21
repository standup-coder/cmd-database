---
{
  "cmd_name": "docker ps",
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
    "docker run",
    "docker inspect"
  ],
  "cmd_tags": [
    "docker",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/docker/docker.yaml"
}
---

# docker ps

> 列出运行中的容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker ps [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a, --all` | 显示所有容器(包括已停止的) |
| `-q, --quiet` | 只显示容器ID |
| `-s, --size` | 显示容器大小 |

## 示例

### 示例 1: 列出运行中的容器

```bash
docker ps
```

### 示例 2: 列出所有容器

```bash
docker ps -a
```

## 关联命令

- [[docker run]]
- [[docker inspect]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
