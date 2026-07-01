---
{
  "cmd_name": "groupadd",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "groupdel",
    "useradd"
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

# groupadd

> 创建用户组

## 用法

```
groupadd [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-g` | 指定 GID |
| `-r` | 创建系统组 |

## 示例

### 示例 1: 创建 developers 组

```bash
sudo groupadd developers
```

### 示例 2: 创建指定 GID 的组

```bash
sudo groupadd -g 1001 ops
```

## 关联命令

- [[groupdel]]
- [[useradd]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
