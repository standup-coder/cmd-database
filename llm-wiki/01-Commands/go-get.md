---
{
  "cmd_name": "go get",
  "cmd_category": "编程语言/Go工具链",
  "cmd_dimension": "Go工具链",
  "cmd_install": "https://go.dev/dl/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "go mod",
    "go build"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/lang/go.yaml"
}
---

# go get

> 添加依赖到当前模块

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go get [packages]
```

## 参数

| Flag | Description |
|------|-------------|
| `-u` | 更新依赖 |
| `-d` | 只下载不安装 |

## 示例

### 示例 1: 添加gin框架

```bash
go get github.com/gin-gonic/gin
```

### 示例 2: 更新所有依赖

```bash
go get -u ./...
```

## 关联命令

- [[go mod]]
- [[go build]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
