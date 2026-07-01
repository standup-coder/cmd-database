---
{
  "cmd_name": "umask",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "chmod",
    "mkdir"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# umask

> 显示或设置默认文件权限掩码

## 用法

```
umask [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | 以符号方式显示 |

## 示例

### 示例 1: 显示当前 umask

```bash
umask
```

### 示例 2: 设置新文件默认权限掩码

```bash
umask 027
```

## 关联命令

- [[chmod]]
- [[mkdir]]

## 风险提示

> ⚠️ **MEDIUM**: umask 设置过大会让新建文件权限过宽，建议按需配置

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
