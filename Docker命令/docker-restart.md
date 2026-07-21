---
{
  "cmd_name": "docker restart",
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
    "docker start",
    "docker stop",
    "docker kill"
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

### 示例 1: 重启容器

```bash
docker restart mycontainer
```

### 示例 2: 30秒优雅重启

```bash
docker restart -t 30 mycontainer
```

## 关联命令

- [[docker-start]]
- [[docker-stop]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
