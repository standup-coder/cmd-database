---
{
  "cmd_name": "env",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "export",
    "printenv"
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

# env

> 显示或修改环境变量后执行命令

## 用法

```
env [OPTIONS] [-] [NAME=VALUE]... [COMMAND [ARGS]]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略继承的环境 |
| `-u` | 删除变量 |

## 示例

### 示例 1: 显示所有环境变量

```bash
env
```

### 示例 2: 临时设置变量后运行程序

```bash
env VAR=value ./app
```

## 关联命令

- [[export]]

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
