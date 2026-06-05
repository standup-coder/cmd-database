---
cmd_name: tail
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- head
- less
- watch
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 显示文件末尾部分，支持实时跟踪
created: '2026-06-04'
source_file: data/os/common.yaml
---
# tail

> 显示文件末尾部分，支持实时跟踪

## 安装

```bash
已预装
```

## 用法

```
tail [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-n <N>` | 显示最后N行（默认10行） |
| `-f` | 实时跟踪文件追加内容 |
| `-F` | 跟踪并处理日志轮转 |

## 示例

### 实时跟踪系统日志

```bash
tail -f /var/log/syslog
```

### 显示文件最后50行

```bash
tail -n 50 file.txt
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
