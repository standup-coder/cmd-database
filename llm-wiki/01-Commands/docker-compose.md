---
{
  "cmd_name": "docker-compose",
  "cmd_category": "容器编排/Docker命令",
  "cmd_dimension": "Docker命令",
  "cmd_install": "pip install docker-compose 或参考官方文档",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "application",
    "docker",
    "intermediate",
    "linux",
    "open-source"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/container/docker/docker.yaml"
}
---

# docker-compose

> 管理多容器应用

## 安装

```bash
pip install docker-compose 或参考官方文档
```

## 用法

```
docker-compose [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `up` | 创建并启动容器 |
| `down` | 停止并删除容器 |
| `ps` | 列出容器 |
| `logs` | 查看日志 |

## 示例

### 示例 1: 后台启动所有服务

```bash
docker-compose up -d
```

### 示例 2: 停止并删除所有服务

```bash
docker-compose down
```

## 参考链接

- [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

## 所属维度

[[Docker命令-MOC|容器编排/Docker命令]]
