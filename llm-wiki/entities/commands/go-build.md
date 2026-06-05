---
cmd_name: go build
cmd_category: 编程语言/Go工具链
cmd_dimension: Go工具链
cmd_install: https://go.dev/dl/
cmd_platforms:
- linux
- darwin
- windows
summary: "编译Go包和依赖"
cmd_level: intermediate
cmd_related:
- go run
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/lang/go.yaml
---


# go build

> 编译Go包和依赖

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go build [packages]
```

## 参数

| Flag | Description |
|------|-------------|
| `-o <file>` | 指定输出文件名 |
| `-v` | 显示编译的包名 |
| `-ldflags` | 传递链接标志 |

## 示例

### 示例 1: 编译当前包

```bash
go build
```

### 示例 2: 编译并指定输出文件名

```bash
go build -o myapp
```

### 示例 3: 编译所有包并显示详细信息

```bash
go build -v ./...
```

## 关联命令

- [[go run]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
