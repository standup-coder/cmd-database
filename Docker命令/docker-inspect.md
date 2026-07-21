---
{
  "cmd_name": "docker inspect",
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
    "docker ps",
    "docker logs",
    "docker exec"
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

# docker inspect

> 获取容器或镜像的底层信息

## 安装

```bash
参考 https://docs.docker.com/engine/install/
```

## 用法

```
docker inspect [OPTIONS] NAME|ID [NAME|ID...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f, --format` | 使用Go模板格式化输出 |
| `-s, --size` | 显示总文件大小 |
| `--type` | 指定对象类型（container/image/network/volume） |

## 示例

### 示例 1: 查看nginx镜像详细信息

```bash
docker inspect nginx
```

### 示例 2: 获取容器IP地址

```bash
docker inspect -f '{{.NetworkSettings.IPAddress}}' mycontainer
```

## 关联命令

- [[docker-ps]]
- [[docker-logs]]
- [[docker-exec]]

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
