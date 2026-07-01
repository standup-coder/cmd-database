---
{
  "cmd_name": "iconv",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "file",
    "enca"
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

# iconv

> 字符编码转换

## 用法

```
iconv [OPTIONS] -f FROM -t TO [INPUT]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 源编码 |
| `-t` | 目标编码 |
| `-o` | 输出文件 |
| `-l` | 列出编码 |

## 示例

### 示例 1: GBK 转 UTF-8

```bash
iconv -f GBK -t UTF-8 input.txt > output.txt
```

### 示例 2: 列出含 GB 的编码

```bash
iconv -l | grep -i gb
```

## 关联命令

- [[file]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
