---
{
  "cmd_name": "pvs",
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
    "vgs"
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

# pvs

> 显示物理卷信息（LVM）

## 用法

```
pvs [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 详细 |
| `-o` | 指定输出列 |

## 示例

### 示例 1: 列出物理卷

```bash
sudo pvs
```

### 示例 2: 显示物理卷与所属卷组

```bash
sudo pvs -o pv_name,vg_name,pv_size
```

## 关联命令

- [[lvs]]
- [[vgs]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
