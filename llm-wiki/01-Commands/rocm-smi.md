---
{
  "cmd_name": "rocm-smi",
  "cmd_category": "硬件/GPU与加速器",
  "cmd_dimension": "GPU与加速器",
  "cmd_install": "随 AMD ROCm 安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nvidia-smi",
    "radeontop"
  ],
  "cmd_tags": [
    "gpu",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/gpu.yaml"
}
---

# rocm-smi

> AMD ROCm GPU 管理

## 安装

```bash
随 AMD ROCm 安装
```

## 用法

```
rocm-smi [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `--showproductname` |  |
| `--showclock` |  |
| `--setfan` |  |
| `--setperflevel` |  |

## 示例

### 示例 1: 显示 AMD GPU 状态

```bash
rocm-smi
```

### 示例 2: 显示产品名

```bash
rocm-smi --showproductname
```

## 关联命令

- [[nvidia-smi]]
- [[radeontop]]

## 风险提示

> ⚠️ **MEDIUM**: 修改风扇或性能等级需谨慎

## 所属维度

[[GPU与加速器-MOC|硬件/GPU与加速器]]
