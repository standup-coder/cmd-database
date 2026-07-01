---
{
  "cmd_name": "lvs",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "vgs",
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

# lvs

> 显示逻辑卷信息（LVM）

## 用法

```
lvs [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 所有 |
| `-o` | 指定输出列 |
| `-v` | 详细 |

## 示例

### 示例 1: 列出逻辑卷

```bash
sudo lvs
```

### 示例 2: 显示底层设备

```bash
sudo lvs -o +devices
```

## 关联命令

- [[vgs]]
- [[pvs]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
