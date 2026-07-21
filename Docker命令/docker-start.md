---
{
  "cmd_name": "docker start",
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
    "docker stop",
    "docker restart",
    "docker run"
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

### 示例 1: 启动已停止的容器

```bash
docker start mycontainer
```

### 示例 2: 启动并查看输出

```bash
docker start -a mycontainer
```

## 关联命令

- [[docker-stop]]
- [[docker-restart]]
- [[docker-run]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
