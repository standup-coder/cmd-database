---
cmd_name: docker exec
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "在运行中的容器内执行命令"
cmd_level: intermediate
cmd_related:
- docker run
cmd_tags:
- docker
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/docker.yaml
---


# docker exec

> 在运行中的容器内执行命令

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-it` | 交互式终端 |
| `-d` | 后台执行 |
| `-u, --user` | 指定用户 |

## 示例

### 示例 1: 进入容器bash终端

```bash
docker exec -it my-container bash
```

### 示例 2: 在容器内执行ls命令

```bash
docker exec my-container ls /app
```

## 关联命令

- [[docker run]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
