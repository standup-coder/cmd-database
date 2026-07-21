---
{
  "cmd_name": "sha256sum",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "md5sum",
    "cksum"
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

# sha256sum

> 计算或校验 SHA-256 校验和

## 用法

```
sha256sum [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 校验 |
| `-b` | 二进制模式 |
| `--tag` | BSD 风格 |

## 示例

### 示例 1: 生成校验文件

```bash
sha256sum file.iso > file.iso.sha256
```

### 示例 2: 校验文件

```bash
sha256sum -c file.iso.sha256
```

## 关联命令

- [[md5sum]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
