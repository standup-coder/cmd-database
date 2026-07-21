---
{
  "cmd_name": "gradle",
  "cmd_category": "构建工具/Gradle",
  "cmd_dimension": "Gradle",
  "cmd_install": "sdk install gradle (macOS) 或 apt install gradle (Ubuntu)",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "mvn",
    "make"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/build-tools/gradle.yaml"
}
---

# gradle

> Gradle 项目自动化构建工具，基于 Groovy/Kotlin DSL

## 安装

```bash
sdk install gradle (macOS) 或 apt install gradle (Ubuntu)
```

## 用法

```
gradle [任务]
```

```
gradle [选项] [任务]
```

## 参数

| Flag | Description |
|------|-------------|
| `--build-cache` | 启用构建缓存 |
| `--parallel` | 并行执行任务 |
| `--no-daemon` | 不使用守护进程 |
| `--info` | 显示日志级别为 INFO |
| `-x` | 显示详细构建日志 |

## 示例

### 示例 1: 构建项目

```bash
gradle build
```

### 示例 2: 运行测试

```bash
gradle test
```

### 示例 3: 无守护进程清理构建

```bash
gradle clean build --no-daemon
```

### 示例 4: 查看项目依赖

```bash
gradle dependencies
```

### 示例 5: 运行 Spring Boot 应用

```bash
gradle bootRun
```

## 关联命令

- [[mvn]]
- [[make]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Gradle-MOC|构建工具/Gradle]]
