---
cmd_name: docker run
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "运行一个新容器"
cmd_level: intermediate
cmd_related:
- docker ps
- docker stop
cmd_tags:
- docker
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/container/docker.yaml
---


# docker run

> 运行一个新容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d, --detach` | 后台运行容器 |
| `-p, --publish` | 端口映射 (host:container) |
| `-v, --volume` | 挂载卷 |
| `--name` | 指定容器名称 |
| `-e, --env` | 设置环境变量 |
| `--rm` | 退出时自动删除容器 |
| `-it` | 交互式终端 |

## 示例

### 示例 1: 后台运行nginx并映射80端口

```bash
docker run -d -p 80:80 nginx
```

### 示例 2: 交互式运行Ubuntu容器

```bash
docker run -it ubuntu bash
```

### 示例 3: 运行后自动删除容器

```bash
docker run --rm alpine echo hello
```

## 关联命令

- [[docker ps]]
- [[docker stop]]

## 参考链接

- [https://docs.docker.com/engine/reference/commandline/run/](https://docs.docker.com/engine/reference/commandline/run/)

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
