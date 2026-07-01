---
{
  "cmd_name": "vgs",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lvs",
    "pvs"
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

# vgs

> 显示卷组信息（LVM）

## 用法

```
vgs [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-o` | 指定输出列 |

## 示例

### 示例 1: 列出卷组

```bash
sudo vgs
```

### 示例 2: 显示卷组大小与空闲

```bash
sudo vgs -o vg_name,vg_size,vg_free
```

## 关联命令

- [[lvs]]
- [[pvs]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
