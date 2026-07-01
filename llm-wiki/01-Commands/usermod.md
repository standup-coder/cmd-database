---
{
  "cmd_name": "usermod",
  "cmd_category": "操作系统/Linux扩展命令",
  "cmd_dimension": "Linux扩展命令",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "useradd",
    "passwd"
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

# usermod

> 修改用户账户

## 用法

```
usermod [OPTIONS] LOGIN
```

## 参数

| Flag | Description |
|------|-------------|
| `-aG` | 添加附加组 |
| `-s` | 修改登录 shell |
| `-L` | 锁定用户 |

## 示例

### 示例 1: 将用户加入 docker 组

```bash
sudo usermod -aG docker alice
```

### 示例 2: 锁定用户账户

```bash
sudo usermod -L alice
```

## 关联命令

- [[useradd]]
- [[passwd]]

## 风险提示

> ⚠️ **MEDIUM**: 修改用户组或锁定账户可能导致无法登录，请谨慎操作

## 所属维度

[[Linux扩展命令-MOC|操作系统/Linux扩展命令]]
