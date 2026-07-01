---
{
  "cmd_name": "su",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sudo",
    "sudo -i"
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

# su

> 切换用户身份

## 用法

```
su [OPTIONS] [LOGIN]
```

## 参数

| Flag | Description |
|------|-------------|
| `-` | 切换环境变量 |
| `-c` | 执行命令后返回 |
| `-s` | 指定 shell |

## 示例

### 示例 1: 完全切换到 alice 环境

```bash
su - alice
```

### 示例 2: 以 alice 执行单条命令

```bash
su -c 'whoami' alice
```

## 关联命令

- [[sudo]]

## 风险提示

> ⚠️ **MEDIUM**: 切换到 root 后操作具有全局影响，请注意命令范围

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
