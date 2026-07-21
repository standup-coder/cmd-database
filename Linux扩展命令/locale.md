---
{
  "cmd_name": "locale",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "localectl",
    "env"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# locale

> 显示和设置区域设置

## 用法

```
locale [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-a` | 列出所有可用区域 |
| `-m` | 列出所有字符映射 |

## 示例

### 示例 1: 显示当前区域设置

```bash
locale
```

### 示例 2: 列出中文区域设置

```bash
locale -a | grep zh_CN
```

## 关联命令

- [[env]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
