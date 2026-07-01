---
{
  "cmd_name": "dnf install",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS 8+/RHEL 8+",
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
  "source_file": "data/os/centos.yaml"
}
---

# dnf install

> Install packages (newer package manager for CentOS 8+)

## 安装

```bash
Pre-installed on CentOS 8+/RHEL 8+
```

## 用法

```
sudo dnf install <package>
```

## 参数

| Flag | Description |
|------|-------------|
| `-y` | Automatic yes to prompts |

## 示例

### 示例 1: Install nginx

```bash
sudo dnf install nginx
```

### 示例 2: Install multiple packages without prompts

```bash
sudo dnf install -y vim git
```

## 风险提示

> ⚠️ **MEDIUM**: Installing from untrusted sources may introduce risks

## 所属维度

[[Operating System-MOC|Operating System]]
