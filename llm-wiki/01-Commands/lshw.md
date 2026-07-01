---
{
  "cmd_name": "lshw",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "包管理器安装，如 sudo apt install lshw",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "dmidecode",
    "inxi"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/info.yaml"
}
---

# lshw

> 列出详细硬件配置

## 安装

```bash
包管理器安装，如 sudo apt install lshw
```

## 用法

```
lshw [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-short` | 简要输出 |
| `-class` | 指定类别 |
| `-json` | JSON 输出 |
| `-sanitize` | 隐藏敏感信息 |

## 示例

### 示例 1: 简要列出硬件

```bash
sudo lshw -short
```

### 示例 2: 只查看内存

```bash
sudo lshw -class memory
```

## 关联命令

- [[dmidecode]]
- [[inxi]]

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
