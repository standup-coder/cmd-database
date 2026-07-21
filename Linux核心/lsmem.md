---
{
  "cmd_name": "lsmem",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "free",
    "lscpu"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-core.yaml"
}
---

# lsmem

> 列出内存信息

## 用法

```
lsmem [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 所有内存 |
| `-o` | 指定输出列 |
| `-b` | 以字节显示 |

## 示例

### 示例 1: 显示内存布局

```bash
lsmem
```

### 示例 2: 显示所有内存信息

```bash
lsmem -a
```

## 关联命令

- [[free]]
- [[lscpu]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
