---
cmd_name: sed
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- awk
- grep
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 流编辑器，执行基本的文本转换
created: '2026-06-04'
source_file: data/os/common.yaml
---
# sed

> 流编辑器，执行基本的文本转换

## 安装

```bash
已预装
```

## 用法

```
sed [选项] '命令' [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-i` | 直接修改文件 |
| `-e` | 执行多个命令 |
| `-n` | 静默模式，只打印指定行 |
| `-r` | 使用扩展正则表达式 |

## 示例

### 全局替换文本

```bash
sed 's/old/new/g' file.txt
```

### 直接修改文件内容

```bash
sed -i 's/old/new/g' file.txt
```

### 打印第5到10行

```bash
sed -n '5,10p' file.txt
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
