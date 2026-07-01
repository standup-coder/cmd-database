---
{
  "cmd_name": "df",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "du",
    "lsblk"
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

# df

> 报告文件系统磁盘空间使用情况

## 用法

```
df [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | 以人类可读方式显示 |
| `-T` | 显示文件系统类型 |

## 示例

### 示例 1: 以人类可读方式查看各分区空间

```bash
df -h
```

### 示例 2: 查看 /var 分区的磁盘使用

```bash
df -h /var
```

## 关联命令

- [[du]]
- [[lsblk]]

## 风险提示

> ⚠️ **LOW**: 只读命令，不会影响系统

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
