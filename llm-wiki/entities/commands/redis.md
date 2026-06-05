---
cmd_name: redis
cmd_category: 数据库工具/Redis工具
cmd_dimension: Redis工具
cmd_install: apt install redis-server (Ubuntu) 或 yum install redis (CentOS)
cmd_platforms:
- linux
- darwin
cmd_level: intermediate
cmd_related:
- redis-cli
- redis-benchmark
- redis-sentinel
cmd_tags:
- linux
- darwin
- intermediate
cmd_risk_level: low
summary: 启动Redis服务器
created: '2026-06-04'
source_file: data/database/redis.yaml
---
# redis

> 启动Redis服务器

## 安装

```bash
apt install redis-server (Ubuntu) 或 yum install redis (CentOS)
```

## 用法

```
redis-server [配置文件] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--port <port>` | 指定监听端口（默认6379） |
| `--daemonize yes` | 后台运行 |
| `--requirepass <password>` | 设置密码 |

## 示例

### 使用配置文件启动Redis

```bash
redis-server /etc/redis/redis.conf
```

### 在6380端口启动Redis

```bash
redis-server --port 6380
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[Redis工具-MOC|数据库工具/Redis工具]]
