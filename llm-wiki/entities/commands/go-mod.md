---
cmd_name: go mod
cmd_category: 编程语言/Go工具链
cmd_dimension: Go工具链
cmd_install: https://go.dev/dl/
cmd_platforms:
- linux
- darwin
- windows
summary: "模块维护"
cmd_level: intermediate
cmd_related:
- go get
- go build
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/go.yaml
---


# go mod

> 模块维护

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go mod <command>
```

## 参数

| Flag | Description |
|------|-------------|
| `init` | 初始化新模块 |
| `tidy` | 整理依赖 |
| `download` | 下载依赖 |
| `verify` | 验证依赖 |

## 示例

### 示例 1: 初始化模块

```bash
go mod init example.com/myapp
```

### 示例 2: 整理依赖

```bash
go mod tidy
```

## 关联命令

- [[go get]]
- [[go build]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
