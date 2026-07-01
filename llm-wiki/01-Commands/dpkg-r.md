---
{
  "cmd_name": "dpkg -r",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on Ubuntu/Debian",
  "cmd_platforms": [
    "linux"
  ],
  "cmd_level": "advanced",
  "cmd_related": [],
  "cmd_tags": [
    "advanced",
    "linux"
  ],
  "cmd_risk_level": "high",
  "created": "2026-05-31",
  "source_file": "data/os/ubuntu.yaml"
}
---

# dpkg -r

> Remove installed package

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo dpkg -r <package>
```

## 示例

### 示例 1: Remove nginx package

```bash
sudo dpkg -r nginx
```

### 示例 2: 彻底移除包及配置

```bash
sudo dpkg -r --purge nginx
```

## 风险提示

> ⚠️ **HIGH**: May leave configuration files; use apt remove instead

## 所属维度

[[Operating System-MOC|Operating System]]
