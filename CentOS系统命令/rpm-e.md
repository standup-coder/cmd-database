---
{
  "cmd_name": "rpm -e",
  "cmd_category": "Operating System",
  "cmd_dimension": "Operating System",
  "cmd_install": "Pre-installed on CentOS/RHEL",
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
  "source_file": "data/os/centos.yaml"
}
---

# rpm -e

> Erase (remove) installed package

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo rpm -e <package>
```

## 示例

### 示例 1: Remove nginx package

```bash
sudo rpm -e nginx
```

### 示例 2: 忽略依赖强制卸载（谨慎使用）

```bash
sudo rpm -e --nodeps nginx
```

## 风险提示

> ⚠️ **HIGH**: May break dependencies; use yum remove instead

## 所属维度

[[通用Linux命令-MOC|Operating System]]
