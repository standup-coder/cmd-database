---
cmd_name: docker images
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "列出本地镜像"
cmd_level: intermediate
cmd_related:
- docker pull
cmd_tags:
- docker
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/docker.yaml
---


# docker images

> 列出本地镜像

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker images [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a, --all` | 显示所有镜像 |
| `-q, --quiet` | 只显示镜像ID |

## 示例

### 示例 1: 列出所有镜像

```bash
docker images
```

### 示例 2: 只显示镜像ID

```bash
docker images -q
```

## 关联命令

- [[docker pull]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
