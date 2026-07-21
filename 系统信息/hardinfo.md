---
{
  "cmd_name": "hardinfo",
  "cmd_category": "硬件/系统信息",
  "cmd_dimension": "系统信息",
  "cmd_install": "包管理器安装，如 sudo apt install hardinfo",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "lshw",
    "inxi"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/hardware/info.yaml"
}
---

# hardinfo

> 图形/命令行系统信息与基准测试

## 安装

```bash
包管理器安装，如 sudo apt install hardinfo
```

## 用法

```
hardinfo [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 生成报告 |
| `-f` | 输出格式 |

## 示例

### 示例 1: 生成 HTML 报告

```bash
hardinfo -r -f html > report.html
```

### 示例 2: 文本报告

```bash
hardinfo -r -f text
```

## 关联命令

- [[lshw]]
- [[inxi]]

## 所属维度

[[系统信息-MOC|硬件/系统信息]]
