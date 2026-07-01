---
{
  "cmd_name": "locate",
  "cmd_category": "操作系统/通用Linux命令",
  "cmd_dimension": "通用Linux命令",
  "cmd_install": "apt install mlocate (Ubuntu) 或 yum install mlocate (CentOS)",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "find",
    "whereis",
    "updatedb"
  ],
  "cmd_tags": [
    "data",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/os/common.yaml"
}
---

# locate

> 通过预建数据库快速查找文件

## 安装

```bash
apt install mlocate (Ubuntu) 或 yum install mlocate (CentOS)
```

## 用法

```
locate [选项] 模式...
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-r` | 使用正则表达式 |
| `-c` | 只显示匹配数量 |
| `-n <N>` | 最多显示N个结果 |

## 示例

### 示例 1: 快速查找nginx配置文件

```bash
locate nginx.conf
```

### 示例 2: 忽略大小写查找日志文件

```bash
locate -i '*.log'
```

## 关联命令

- [[find]]
- [[whereis]]

## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
