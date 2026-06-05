---
cmd_name: trash
cmd_category: 操作系统/通用Linux命令
cmd_dimension: 通用Linux命令
cmd_install: pip install trash-cli (跨平台) 或 apt install trash-cli (Ubuntu)
cmd_platforms:
- linux
- darwin
cmd_level: intermediate
cmd_related:
- rm
- mv
- rmdir
cmd_tags:
- linux
- darwin
- intermediate
cmd_risk_level: low
summary: 将文件移动到回收站而非永久删除
created: '2026-06-04'
source_file: data/os/common.yaml
---
# trash

> 将文件移动到回收站而非永久删除

## 安装

```bash
pip install trash-cli (跨平台) 或 apt install trash-cli (Ubuntu)
```

## 用法

```
trash [选项] 文件...
```

## 参数

| Flag | Description |
|------|-------------|
| `-v, --verbose` | 显示每个被删除的文件 |
| `-f, --force` | 忽略不存在的文件 |

## 示例

### 将file.txt移入回收站

```bash
trash file.txt
```

### 批量移入回收站

```bash
trash *.log
```

### 列出回收站中的文件

```bash
trash-list
```

### 清空回收站

```bash
trash-empty
```

## 风险提示

> ⚠️ **LOW**: 基本命令，低风险操作

## 参考链接



## 所属维度

[[通用Linux命令-MOC|操作系统/通用Linux命令]]
