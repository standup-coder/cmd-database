---
cmd_name: egrep
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
- fgrep
- awk
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 扩展正则表达式grep（等同于grep -E）
created: '2026-06-04'
source_file: data/os/common.yaml
---
# egrep

> 扩展正则表达式grep（等同于grep -E）

## 安装

```bash
已预装
```

## 用法

```
egrep [选项] 模式 [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 忽略大小写 |
| `-v` | 反向匹配 |
| `-n` | 显示行号 |

## 示例

### 匹配error或warning

```bash
egrep 'error|warning' log.txt
```

### 匹配邮箱格式

```bash
egrep -i '^[a-z]+@[a-z]+\.com' emails.txt
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
