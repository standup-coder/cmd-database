---
{
  "cmd_name": "radeontop",
  "cmd_category": "硬件/GPU与加速器",
  "cmd_dimension": "GPU与加速器",
  "cmd_install": "包管理器安装，如 sudo apt install radeontop",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "rocm-smi",
    "intel-gpu-top"
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

# radeontop

> AMD GPU 占用监控

## 安装

```bash
包管理器安装，如 sudo apt install radeontop
```

## 用法

```
radeontop [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-d` | 守护模式 |
| `-s` | 采样 |
| `-t` | 透明度 |

## 示例

### 示例 1: 实时监控 AMD GPU

```bash
sudo radeontop
```

### 示例 2: 记录到文件

```bash
sudo radeontop -d /tmp/radeontop.log
```

## 关联命令

- [[rocm-smi]]
- [[intel-gpu-top]]

## 所属维度

[[GPU与加速器-MOC|硬件/GPU与加速器]]
