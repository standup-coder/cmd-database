---
{
  "cmd_name": "go install",
  "cmd_category": "编程语言/Go工具链",
  "cmd_dimension": "Go工具链",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "go get",
    "go build",
    "go run"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/go.yaml"
}
---

# go install

> 编译并安装Go包到$GOPATH/bin

## 用法

```
go install [选项] [包路径]@版本
```

## 参数

| Flag | Description |
|------|-------------|
| `-x` | 打印执行的命令 |

## 示例

### 示例 1: 安装最新版goimports

```bash
go install golang.org/x/tools/cmd/goimports@latest
```

### 示例 2: 安装当前项目的命令

```bash
go install ./cmd/myapp
```

## 关联命令

- [[go-get]]
- [[go-build]]
- [[go-run]]

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
