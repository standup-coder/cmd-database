---
{
  "cmd_name": "md5sum",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sha256sum",
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

# md5sum

> 计算或校验 MD5 校验和

## 用法

```
md5sum [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 校验 |
| `--quiet` | 只显示错误 |

## 示例

### 示例 1: 计算 MD5

```bash
md5sum file.txt
```

### 示例 2: 校验 MD5

```bash
md5sum -c checksum.md5
```

## 关联命令

- [[sha256sum]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
