---
{
  "cmd_name": "apt install",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu/Debian",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# apt install

> Install new packages

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo apt install <package>
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | Automatic yes to prompts |

## 示例

### 示例 1: Install nginx web server

```bash
sudo apt install nginx
```

### 示例 2: Install multiple packages

```bash
sudo apt install vim git curl -y
```

## 风险提示

> ⚠️ **MEDIUM**: Installing from untrusted repositories may introduce security risks

## 所属维度

[[通用Linux命令-MOC|Operating System]]
