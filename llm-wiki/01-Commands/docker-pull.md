---
{
  "cmd_name": "docker pull",
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
    "docker push",
    "docker images"
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

# docker pull

> 从镜像仓库拉取镜像

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker pull [OPTIONS] NAME[:TAG]
```

## 示例

### 示例 1: 拉取nginx最新镜像

```bash
docker pull nginx
```

### 示例 2: 拉取指定版本

```bash
docker pull nginx:1.21
```

## 关联命令

- [[docker push]]
- [[docker images]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
