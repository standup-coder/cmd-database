---
{
  "cmd_name": "gradlew",
  "cmd_category": "构建工具/Gradle",
  "cmd_dimension": "Gradle",
  "cmd_install": "",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gradle",
    "gradle init"
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

# gradlew

> Gradle Wrapper 脚本，确保使用项目指定的 Gradle 版本

## 用法

```
./gradlew [任务]
```

```
gradlew.bat [任务] (Windows)
```

## 示例

### 示例 1: 使用 wrapper 构建

```bash
./gradlew build
```

### 示例 2: 使用 wrapper 运行测试

```bash
./gradlew test
```

## 关联命令

- [[gradle]]
- [[gradle-init]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Gradle-MOC|构建工具/Gradle]]
