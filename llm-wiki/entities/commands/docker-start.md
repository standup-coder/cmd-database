---
cmd_name: docker start
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- docker stop
- docker restart
- docker run
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 启动一个或多个已停止的容器
created: '2026-06-04'
source_file: data/container/docker.yaml
---
# docker start

> 启动一个或多个已停止的容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker start [OPTIONS] CONTAINER [CONTAINER...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a, --attach` | 附加到容器的标准输出 |
| `-i, --interactive` | 附加标准输入 |

## 示例

### 启动已停止的容器

```bash
docker start mycontainer
```

### 启动并查看输出

```bash
docker start -a mycontainer
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
