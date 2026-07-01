---
{
  "cmd_name": "intel-gpu-top",
  "cmd_category": "硬件/GPU与加速器",
  "cmd_dimension": "GPU与加速器",
  "cmd_install": "包管理器安装 intel-gpu-tools",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "radeontop",
    "nvidia-smi"
  ],
  "cmd_tags": [
    "monitoring",
    "gpu",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/gpu.yaml"
}
---

# intel-gpu-top

> Intel GPU 占用监控

## 安装

```bash
包管理器安装 intel-gpu-tools
```

## 用法

```
intel-gpu-top [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-s` | 采样 |
| `-o` | 输出文件 |

## 示例

### 示例 1: 实时监控 Intel GPU

```bash
sudo intel-gpu-top
```

### 示例 2: 每秒采样

```bash
sudo intel-gpu-top -s 1000
```

## 关联命令

- [[radeontop]]
- [[nvidia-smi]]

## 所属维度

[[GPU与加速器-MOC|硬件/GPU与加速器]]
