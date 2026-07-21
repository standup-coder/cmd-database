---
{
  "cmd_name": "ssh",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "scp",
    "sftp",
    "rsync"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# ssh

> OpenSSH 远程登录客户端

## 用法

```
ssh [OPTIONS] [USER@]HOST [COMMAND]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 指定端口 |
| `-i` | 指定私钥文件 |
| `-L` | 本地端口转发 |

## 示例

### 示例 1: 登录远程服务器

```bash
ssh user@192.168.1.10
```

### 示例 2: 使用指定私钥和端口登录

```bash
ssh -i ~/.ssh/id_rsa -p 2222 user@host
```

## 关联命令

- [[scp]]
- [[rsync]]

## 风险提示

> ⚠️ **MEDIUM**: 请确认主机指纹和私钥安全，避免连接到被篡改的服务器

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
