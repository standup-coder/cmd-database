---
cmd_name: go vet
cmd_category: 编程语言/Go工具链
cmd_dimension: Go工具链
cmd_install: https://go.dev/dl/
cmd_platforms:
- linux
- darwin
- windows
summary: "检查Go代码中的常见错误"
cmd_level: intermediate
cmd_related:
- go test
- go fmt
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/lang/go.yaml
---


# go vet

> 检查Go代码中的常见错误

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go vet [packages]
```

## 示例

### 示例 1: 检查所有包

```bash
go vet ./...
```

## 关联命令

- [[go test]]
- [[go fmt]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
