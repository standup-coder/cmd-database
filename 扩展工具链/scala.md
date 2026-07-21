---
{
  "cmd_name": "scala",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "参考 https://www.scala-lang.org/download/",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "sbt",
    "java"
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

# scala

> Scala 解释器与运行器

## 安装

```bash
参考 https://www.scala-lang.org/download/
```

## 用法

```
scala [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-version` |  |
| `-cp` | 类路径 |
| `-D` | 系统属性 |

## 示例

### 示例 1: 查看版本

```bash
scala -version
```

### 示例 2: 运行 Scala 脚本

```bash
scala Hello.scala
```

## 关联命令

- [[sbt]]
- [[java]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
