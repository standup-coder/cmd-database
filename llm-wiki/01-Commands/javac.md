---
{
  "cmd_name": "javac",
  "cmd_category": "编程语言/Java工具链",
  "cmd_dimension": "Java工具链",
  "cmd_install": "下载JDK: https://adoptium.net/",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/java.yaml"
}
---

# javac

> 编译Java源代码

## 安装

```bash
下载JDK: https://adoptium.net/
```

## 用法

```
javac [options] <source files>
```

## 参数

| Flag | Description |
|------|-------------|
| `-d <directory>` | 指定输出目录 |
| `-cp, -classpath` | 指定类路径 |
| `-encoding` | 指定源文件编码 |

## 示例

### 示例 1: 编译Java文件

```bash
javac HelloWorld.java
```

### 示例 2: 编译到bin目录

```bash
javac -d bin src/*.java
```

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]
