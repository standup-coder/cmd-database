---
{
  "cmd_name": "man",
  "cmd_category": "操作系统/Linux核心",
  "cmd_dimension": "Linux核心",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "info",
    "whatis"
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

# man

> 查看命令/函数手册页

## 用法

```
man [OPTIONS] [SECTION] NAME
```

## 参数

| Flag | Description |
|------|-------------|
| `-k` | 关键字搜索 |
| `-f` | 同 whatis |
| `-a` | 显示所有匹配节 |

## 示例

### 示例 1: 查看 ls 手册

```bash
man ls
```

### 示例 2: 查看配置文件格式

```bash
man 5 passwd
```

## 关联命令

- [[whatis]]

## 所属维度

[[Linux核心-MOC|操作系统/Linux核心]]
