---
{
  "cmd_name": "nvidia-smi",
  "cmd_category": "硬件/GPU与加速器",
  "cmd_dimension": "GPU与加速器",
  "cmd_install": "随 NVIDIA 驱动安装",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nvtop",
    "rocm-smi"
  ],
  "cmd_tags": [
    "monitoring",
    "gpu",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/hardware/gpu.yaml"
}
---

# nvidia-smi

> NVIDIA GPU 管理与监控

## 安装

```bash
随 NVIDIA 驱动安装
```

## 用法

```
nvidia-smi [OPTIONS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-L` | 列出 GPU |
| `-q` | 查询 |
| `-dmon` | 监控 |
| `-pl` | 设置功耗限制 |
| `-i` | 指定 GPU |

## 示例

### 示例 1: 显示 GPU 状态

```bash
nvidia-smi
```

### 示例 2: 监控功耗/温度/显存

```bash
nvidia-smi dmon -s pucm
```

## 关联命令

- [[rocm-smi]]

## 风险提示

> ⚠️ **MEDIUM**: 修改功耗/频率限制可能影响稳定性或硬件寿命

## 所属维度

[[GPU与加速器-MOC|硬件/GPU与加速器]]
