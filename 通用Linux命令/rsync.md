---
{
  "cmd_name": "rsync",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "apt install rsync (Ubuntu) 或 yum install rsync (CentOS)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "unix"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "scp",
    "cp",
    "sftp"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# rsync

> 远程和本地文件同步工具，支持增量传输

## 安装

```bash
apt install rsync (Ubuntu) 或 yum install rsync (CentOS)
```

## 用法

```
rsync [选项] 源 目标
```

## 参数

| Flag | Description |
|------|-------------|
| `-a, --archive` | 归档模式，保留权限和属性 |
| `-v, --verbose` | 显示详细输出 |
| `-z, --compress` | 传输时压缩数据 |
| `-P` | 显示进度并支持断点续传 |
| `--delete` | 删除目标中源没有的文件 |
| `-e ssh` | 使用SSH作为传输通道 |

## 示例

### 示例 1: 同步本地目录到远程

```bash
rsync -avz /local/dir/ user@remote:/remote/dir/
```

### 示例 2: 镜像同步，删除目标多余文件

```bash
rsync -avz --delete /src/ /dest/
```

## 关联命令

- [[scp]]
- [[cp]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
