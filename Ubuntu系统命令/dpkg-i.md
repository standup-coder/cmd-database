---
{
  "cmd_name": "dpkg -i",
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

# dpkg -i

> Install .deb package file

## 安装

```bash
Pre-installed on Ubuntu/Debian
```

## 用法

```
sudo dpkg -i <package.deb>
```

## 示例

### 示例 1: Install local .deb file

```bash
sudo dpkg -i package.deb
```

### 示例 2: 安装时保留旧配置文件

```bash
sudo dpkg -i --force-confold package.deb
```

## 风险提示

> ⚠️ **HIGH**: Installing untrusted .deb files may compromise system

## 所属维度

[[通用Linux命令-MOC|Operating System]]
