---
{
  "cmd_name": "rpm -i",
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

# rpm -i

> Install RPM package file

## 安装

```bash
Pre-installed on CentOS/RHEL
```

## 用法

```
sudo rpm -i <package.rpm>
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | Verbose output |
| `-h` | Print hash marks during installation |

## 示例

### 示例 1: Install RPM with progress

```bash
sudo rpm -ivh package.rpm
```

### 示例 2: 忽略依赖强制安装（谨慎使用）

```bash
sudo rpm -ivh --nodeps package.rpm
```

## 风险提示

> ⚠️ **HIGH**: Installing untrusted RPM files may compromise system

## 所属维度

[[通用Linux命令-MOC|Operating System]]
