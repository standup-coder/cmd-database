---
cmd_name: docker attach
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- docker exec
- docker run
- docker logs
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 附加到正在运行的容器
created: '2026-06-04'
source_file: data/container/docker.yaml
---
# docker attach

> 附加到正在运行的容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker attach [OPTIONS] CONTAINER
```

## 参数

| Flag | Description |
|------|-------------|
| `--detach-keys` | 覆盖分离序列键 |
| `--no-stdin` | 不附加标准输入 |
| `--sig-proxy` | 代理所有接收到的信号（默认true） |

## 示例

### 附加到运行中的容器

```bash
docker attach mycontainer
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
