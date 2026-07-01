---
{
  "cmd_name": "du",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "df",
    "ls"
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

# du

> 估算文件和目录的磁盘使用空间

## 用法

```
du [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | 以人类可读方式显示 |
| `-s` | 只显示总计 |
| `--max-depth` | 限制目录递归深度 |

## 示例

### 示例 1: 查看 /var/log 总大小

```bash
du -sh /var/log
```

### 示例 2: 查看 /home 下各一级目录大小

```bash
du -h --max-depth=1 /home
```

## 关联命令

- [[df]]
- [[ls]]

## 风险提示

> ⚠️ **LOW**: 大量小文件目录可能执行较慢，但不修改数据

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
