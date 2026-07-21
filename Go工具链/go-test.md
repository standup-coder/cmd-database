---
{
  "cmd_name": "go test",
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
    "go build",
    "go vet"
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

# go test

> 运行测试

## 安装

```bash
https://go.dev/dl/
```

## 用法

```
go test [packages]
```

## 参数

| Flag | Description |
|------|-------------|
| `-v` | 显示详细输出 |
| `-cover` | 显示测试覆盖率 |
| `-run <pattern>` | 运行匹配的测试 |
| `-bench <pattern>` | 运行性能测试 |

## 示例

### 示例 1: 运行当前包的测试

```bash
go test
```

### 示例 2: 运行所有包的测试

```bash
go test -v ./...
```

### 示例 3: 运行测试并显示覆盖率

```bash
go test -cover
```

## 关联命令

- [[go build]]
- [[go vet]]

## 风险提示

> ⚠️ **LOW**: 常规操作，无特殊风险

## 所属维度

[[Go工具链-MOC|编程语言/Go工具链]]
