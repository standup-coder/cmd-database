---
cmd_name: docker logs
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
summary: "查看容器日志"
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


# docker logs

> 查看容器日志

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker logs [OPTIONS] CONTAINER
```

## 参数

| Flag | Description |
|------|-------------|
| `-f, --follow` | 实时跟踪日志 |
| `--tail <n>` | 显示最后n行 |
| `-t, --timestamps` | 显示时间戳 |

## 示例

### 示例 1: 查看容器日志

```bash
docker logs my-container
```

### 示例 2: 实时查看最后100行日志

```bash
docker logs -f --tail 100 my-container
```

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
