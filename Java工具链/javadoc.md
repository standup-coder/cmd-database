---
{
  "cmd_name": "javadoc",
  "cmd_category": "编程语言/Java工具链",
  "cmd_dimension": "Java工具链",
  "cmd_install": "JDK自带工具",
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

# javadoc

> 生成Java文档

## 安装

```bash
JDK自带工具
```

## 用法

```
javadoc [options] <source files>
```

## 参数

| Flag | Description |
|------|-------------|
| `-d <directory>` | 指定输出目录 |
| `-author` | 包含作者信息 |
| `-version` | 包含版本信息 |

## 示例

### 示例 1: 生成文档到docs目录

```bash
javadoc -d docs src/*.java
```

### 示例 2: 生成包含私有成员的文档

```bash
javadoc -private -d docs src/main/java/com/example/*.java
```

## 所属维度

[[Java工具链-MOC|编程语言/Java工具链]]
