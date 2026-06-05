---
cmd_name: fgrep
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- grep
- egrep
- awk
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 固定字符串grep（等同于grep -F），禁用正则表达式
created: '2026-06-04'
source_file: data/os/common.yaml
---
# fgrep

> 固定字符串grep（等同于grep -F），禁用正则表达式

## 安装

```bash
已预装
```

## 用法

```
fgrep [选项] 字符串 [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-x` | 整行匹配 |
| `-f` | 从文件读取匹配模式 |

## 示例

### 按字面匹配a*b（不解释正则）

```bash
fgrep 'a*b' file.txt
```

### 从文件读取多个匹配字符串

```bash
fgrep -f patterns.txt log.txt
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
