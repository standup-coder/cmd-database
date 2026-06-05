---
cmd_name: docker restart
cmd_category: 容器编排/Docker命令
cmd_dimension: Docker命令
cmd_install: 参考 https://docs.docker.com/engine/install/
cmd_platforms:
- linux
- darwin
- windows
cmd_level: intermediate
cmd_related:
- docker start
- docker stop
cmd_tags:
- linux
- darwin
- windows
- intermediate
cmd_risk_level: low
summary: 重启一个或多个容器
created: '2026-06-04'
source_file: data/container/docker.yaml
---
# docker restart

> 重启一个或多个容器

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-t, --time` | 关闭前等待的秒数（默认10秒） |

## 示例

### 重启容器

```bash
docker restart mycontainer
```

### 30秒优雅重启

```bash
docker restart -t 30 mycontainer
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
