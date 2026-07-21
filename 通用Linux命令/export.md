---
{
  "cmd_name": "export",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "unix"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "env",
    "set",
    "unset"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# export

> 设置或显示环境变量

## 用法

```
export [选项] [名称[=值]...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-p` | 以可复用格式显示所有变量 |
| `-n` | 从导出列表中移除变量 |

## 示例

### 示例 1: 添加路径到PATH

```bash
export PATH=$PATH:/usr/local/bin
```

### 示例 2: 设置环境变量

```bash
export MY_VAR=value
```

### 示例 3: 显示所有导出的变量

```bash
export -p
```

## 关联命令

- [[env]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
