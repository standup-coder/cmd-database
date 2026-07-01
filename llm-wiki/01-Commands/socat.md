---
{
  "cmd_name": "socat",
  "cmd_category": "网络工具/扩展工具",
  "cmd_dimension": "扩展工具",
  "cmd_install": "包管理器安装，如 sudo apt install socat",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nc",
    "ssh -L"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/network/tools-extra.yaml"
}
---

# socat

> 双向数据转发工具，号称 netcat 增强版

## 安装

```bash
包管理器安装，如 sudo apt install socat
```

## 用法

```
socat [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 单向模式 |
| `-d` | 增加调试级别 |
| `TCP-LISTEN` |  |
| `TCP` |  |

## 示例

### 示例 1: 将本地 8080 转发到远程 80

```bash
socat TCP-LISTEN:8080,fork TCP:192.168.1.10:80
```

### 示例 2: 通过 socat 连接 Docker socket

```bash
socat - UNIX-CONNECT:/var/run/docker.sock
```

## 关联命令

- [[nc]]

## 风险提示

> ⚠️ **MEDIUM**: 端口转发会暴露内部服务，请确认访问控制和防火墙

## 所属维度

[[扩展工具-MOC|网络工具/扩展工具]]
