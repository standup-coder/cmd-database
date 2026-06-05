---
cmd_name: docker rmi
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- docker images
- docker pull
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 删除本地镜像
created: '2026-06-04'
source_file: data/container/docker.yaml
---
# docker rmi

> 删除本地镜像

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f, --force` | 强制删除镜像 |
| `--no-prune` | 不删除未标记的父镜像 |

## 示例

### 删除指定镜像

```bash
docker rmi nginx:latest
```

### 删除所有悬空镜像

```bash
docker rmi $(docker images -q -f dangling=true)
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
