---
cmd_name: mvn archetype
cmd_category: 构建工具/Maven
cmd_dimension: Maven
cmd_install: 同 mvn
cmd_platforms:
- linux
- darwin
- windows
summary: "Maven 项目原型生成工具"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/build/maven.yaml
---


# mvn archetype

> Maven 项目原型生成工具

## 安装

```bash
同 mvn
```

## 用法

```
mvn archetype:generate -DgroupId=... -DartifactId=...
```

## 示例

### 示例 1: 生成 Maven 快速启动项目

```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart
```

## 所属维度

[[Maven-MOC|构建工具/Maven]]
