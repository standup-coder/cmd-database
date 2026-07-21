---
{
  "cmd_name": "visudo",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "sudo",
    "usermod"
  ],
  "cmd_tags": [
    "safety",
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "critical",
  "created": "2026-05-31",
  "source_file": "data/os/linux-extra.yaml"
}
---

# visudo

> 安全编辑 sudoers 文件

## 用法

```
visudo [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-c` | 检查 sudoers 语法 |
| `-f` | 指定 sudoers 文件 |

## 示例

### 示例 1: 编辑 /etc/sudoers

```bash
sudo visudo
```

### 示例 2: 检查 sudoers 语法

```bash
sudo visudo -c
```

## 关联命令

- [[sudo]]
- [[usermod]]

## 风险提示

> ⚠️ **CRITICAL**: 错误的 sudoers 配置可能导致无法提权或权限过大，编辑前请备份

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
