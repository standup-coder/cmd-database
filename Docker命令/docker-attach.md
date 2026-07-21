---
{
  "cmd_name": "docker attach",
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
    "docker exec",
    "docker run",
    "docker logs"
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

### 示例 1: 附加到运行中的容器

```bash
docker attach mycontainer
```

### 示例 2: 附加时忽略键盘中断转发

```bash
docker attach --sig-proxy=false mycontainer
```

## 关联命令

- [[docker-exec]]
- [[docker-run]]
- [[docker-logs]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
