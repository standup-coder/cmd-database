---
{
  "cmd_name": "clinfo",
  "cmd_category": "硬件/GPU与加速器",
  "cmd_dimension": "GPU与加速器",
  "cmd_install": "包管理器安装，如 sudo apt install clinfo",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nvidia-smi",
    "rocm-smi"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/gpu.yaml"
}
---

# clinfo

> 显示 OpenCL 平台与设备信息

## 安装

```bash
包管理器安装，如 sudo apt install clinfo
```

## 用法

```
clinfo [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-l` | 简要 |
| `-a` | 全部 |

## 示例

### 示例 1: 显示 OpenCL 信息

```bash
clinfo
```

### 示例 2: 简要列出平台设备

```bash
clinfo -l
```

## 关联命令

- [[nvidia-smi]]
- [[rocm-smi]]

## 所属维度

[[GPU与加速器-MOC|硬件/GPU与加速器]]
