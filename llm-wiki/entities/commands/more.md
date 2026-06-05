---
cmd_name: more
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: ''
cmd_platforms:
- linux
- darwin
- unix
cmd_level: intermediate
cmd_related:
- less
- cat
- head
cmd_tags:
- linux
- darwin
- unix
- intermediate
cmd_risk_level: low
summary: 分页查看文件内容（less的简化版）
created: '2026-06-04'
source_file: data/os/common.yaml
---
# more

> 分页查看文件内容（less的简化版）

## 安装

```bash
已预装
```

## 用法

```
more [选项] [文件...]
```

## 参数

| Flag | Description |
|------|-------------|
| `-N` | 显示行号 |
| `+N` | 从第N行开始显示 |

## 示例

### 分页查看文件

```bash
more file.txt
```

### 管道分页查看

```bash
cat file.txt | more
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
