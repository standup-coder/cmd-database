---
cmd_name: locate
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: apt install mlocate (Ubuntu) 或 yum install mlocate (CentOS)
cmd_platforms:
- linux
- darwin
cmd_level: intermediate
cmd_related:
- find
- whereis
cmd_tags:
- linux
- darwin
- intermediate
cmd_risk_level: low
summary: 通过预建数据库快速查找文件
created: '2026-06-04'
source_file: data/os/common.yaml
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

### 快速查找nginx配置文件

```bash
locate nginx.conf
```

### 忽略大小写查找日志文件

```bash
locate -i '*.log'
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
