---
{
  "cmd_name": "sudo",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "advanced",
  "cmd_related": [
    "su",
    "passwd"
  ],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# sudo

> 以超级用户或其他用户身份执行命令

## 用法

```
sudo [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 以指定用户身份执行 |
| `-i` | 模拟初始登录的 root shell |
| `-l` | 列出当前用户可执行的命令 |

## 示例

### 示例 1: 以 root 权限重启服务

```bash
sudo systemctl restart nginx
```

### 示例 2: 切换到 postgres 用户执行 psql

```bash
sudo -u postgres psql
```

## 关联命令

- [[su]]
- [[passwd]]

## 风险提示

> ⚠️ **HIGH**: root 权限操作具有破坏性，请确认命令和影响范围

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
