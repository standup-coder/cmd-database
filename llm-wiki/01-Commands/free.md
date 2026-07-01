---
{
  "cmd_name": "free",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "top",
    "vmstat"
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

# free

> 显示系统内存使用情况

## 用法

```
free [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-h` | 以人类可读方式显示 |
| `-m` | 以 MB 显示 |
| `-g` | 以 GB 显示 |

## 示例

### 示例 1: 人类可读方式查看内存

```bash
free -h
```

### 示例 2: 以 MB 查看内存

```bash
free -m
```

## 风险提示

> ⚠️ **LOW**: 只读命令

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
