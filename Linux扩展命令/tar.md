---
{
  "cmd_name": "tar",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gzip",
    "zip"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# tar

> 归档和压缩工具

## 用法

```
tar [OPTIONS] [ARCHIVE] [FILE...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 创建归档 |
| `-x` | 解压归档 |
| `-z` | 使用 gzip |
| `-f` | 指定文件名 |
| `-v` | 显示过程 |

## 示例

### 示例 1: 压缩 /etc 目录

```bash
tar -czvf backup.tar.gz /etc
```

### 示例 2: 解压到 /tmp

```bash
tar -xzvf backup.tar.gz -C /tmp
```

## 关联命令

- [[gzip]]
- [[zip]]

## 风险提示

> ⚠️ **MEDIUM**: 解压到错误目录或覆盖现有文件会造成混乱，请确认目标路径

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
