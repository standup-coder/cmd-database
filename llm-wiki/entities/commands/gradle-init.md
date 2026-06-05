---
cmd_name: gradle init
cmd_category: 构建工具/Gradle
cmd_dimension: Gradle
cmd_install: 同 gradle
cmd_platforms:
- linux
- darwin
- windows
summary: "Gradle Wrapper 初始化，生成 gradlew 脚本"
cmd_level: intermediate
cmd_related:
- gradle
- gradlew
cmd_tags:
- intermediate
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/build/gradle.yaml
---


# gradle init

> Gradle Wrapper 初始化，生成 gradlew 脚本

## 安装

```bash
同 gradle
```

## 用法

```
gradle wrapper --gradle-version 8.5
```

## 示例

### 示例 1: 生成指定版本的 Gradle Wrapper

```bash
gradle wrapper --gradle-version 8.5
```

## 关联命令

- [[gradle]]
- [[gradlew]]

## 风险提示

> ⚠️ **MEDIUM**: 会修改本地环境或依赖

## 所属维度

[[Gradle-MOC|构建工具/Gradle]]
