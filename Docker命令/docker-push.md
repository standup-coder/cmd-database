---
{
  "cmd_name": "docker push",
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
    "docker pull",
    "docker build",
    "docker tag"
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

# docker push

> 将本地镜像推送到镜像仓库

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker push [OPTIONS] NAME[:TAG]
```

## 参数

| Flag | Description |
|------|-------------|
| `--all-tags` | 推送所有标签 |
| `--disable-content-trust` | 跳过镜像签名验证 |

## 示例

### 示例 1: 推送镜像到仓库

```bash
docker push myrepo/myimage:latest
```

### 示例 2: 推送带标签的镜像

```bash
docker push username/nginx:v1.0
```

## 关联命令

- [[docker pull]]
- [[docker build]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
