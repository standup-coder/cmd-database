---
{
  "cmd_name": "memcached",
  "cmd_category": "数据库工具/扩展命令",
  "cmd_dimension": "扩展命令",
  "cmd_install": "包管理器安装，如 sudo apt install memcached",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "redis-cli",
    "telnet"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/database/more.yaml"
}
---

# memcached

> Memcached 内存对象缓存守护进程

## 安装

```bash
包管理器安装，如 sudo apt install memcached
```

## 用法

```
memcached [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 端口 |
| `-m` | 内存大小 |
| `-d` | 守护进程 |
| `-l` | 监听地址 |

## 示例

### 示例 1: 启动 memcached

```bash
memcached -m 64 -p 11211 -u nobody -l 127.0.0.1
```

### 示例 2: 后台运行 128MB 缓存

```bash
memcached -d -m 128 -c 1024
```

## 关联命令

- [[redis-cli]]
- [[telnet]]

## 风险提示

> ⚠️ **MEDIUM**: 默认无认证，请勿直接暴露到公网，建议使用 SASL 或防火墙

## 所属维度

[[扩展命令-MOC|数据库工具/扩展命令]]
