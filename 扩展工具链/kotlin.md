---
{
  "cmd_name": "kotlin",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "参考 https://kotlinlang.org/docs/command-line.html",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "java",
    "gradle"
  ],
  "cmd_tags": [
    "compiler",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/more.yaml"
}
---

# kotlin

> Kotlin 命令行编译器

## 安装

```bash
参考 https://kotlinlang.org/docs/command-line.html
```

## 用法

```
kotlin [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `-version` |  |
| `-cp` |  |
| `-d` | 输出 |

## 示例

### 示例 1: 编译为 jar

```bash
kotlinc Hello.kt -include-runtime -d hello.jar
```

### 示例 2: 运行

```bash
kotlin hello.jar
```

## 关联命令

- [[java]]
- [[gradle]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
