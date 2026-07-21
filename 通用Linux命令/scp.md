---
{
  "cmd_name": "scp",
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
    "ssh",
    "rsync",
    "sftp"
  ],
  "cmd_tags": [
    "safety",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# scp

> 基于 SSH 的安全文件复制

## 用法

```
scp [OPTIONS] SOURCE TARGET
```

## 参数

| Flag | Description |
|------|-------------|
| `-P` | 指定远程端口（注意大写） |
| `-r` | 递归复制目录 |
| `-i` | 指定私钥文件 |

## 示例

### 示例 1: 上传文件到远程服务器

```bash
scp file.txt user@host:/home/user/
```

### 示例 2: 递归下载远程目录

```bash
scp -r user@host:/data ./backup
```

## 关联命令

- [[ssh]]
- [[rsync]]

## 风险提示

> ⚠️ **MEDIUM**: 覆盖目标文件不会提示，请确认目标路径

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
