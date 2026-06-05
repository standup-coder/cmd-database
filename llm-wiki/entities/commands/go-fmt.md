---
cmd_name: go fmt
cmd_category: 编程语言/Go工具链
cmd_dimension: Go工具链
cmd_install: https://go.dev/dl/
cmd_platforms:
- linux
- darwin
- windows
summary: "格式化Go代码"
cmd_level: intermediate
cmd_related:
- go vet
- go build
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/go.yaml
---


# go fmt

> 格式化Go代码

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go fmt [packages]
```

## 示例

### 示例 1: 格式化所有Go文件

```bash
go fmt ./...
```

## 关联命令

- [[go vet]]
- [[go build]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
