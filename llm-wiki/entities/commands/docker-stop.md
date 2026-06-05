---
cmd_name: docker stop
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "停止运行中的容器"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- docker
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/docker.yaml
---


# docker stop

> 停止运行中的容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t, --time` | 超时时间(秒) |

## 示例

### 示例 1: 停止指定容器

```bash
docker stop my-container
```

### 示例 2: 停止所有运行中的容器

```bash
docker stop $(docker ps -q)
```

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
