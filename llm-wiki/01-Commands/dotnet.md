---
{
  "cmd_name": "dotnet",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "参考 https://dotnet.microsoft.com/download",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "nuget",
    "msbuild"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/more.yaml"
}
---

# dotnet

> .NET 命令行工具

## 安装

```bash
参考 https://dotnet.microsoft.com/download
```

## 用法

```
dotnet [OPTIONS] COMMAND
```

## 参数

| Flag | Description |
|------|-------------|
| `new` | 创建项目 |
| `build` | 构建 |
| `run` | 运行 |
| `publish` | 发布 |
| `add` | package |

## 示例

### 示例 1: 创建控制台项目

```bash
dotnet new console -o MyApp
```

### 示例 2: 构建项目

```bash
dotnet build
```

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
