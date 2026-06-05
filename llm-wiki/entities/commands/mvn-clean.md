---
cmd_name: mvn clean
cmd_category: 构建工具/Maven
cmd_dimension: Maven
cmd_install: 同 mvn
cmd_platforms:
- linux
- darwin
- windows
summary: "清理构建输出目录(target)"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/build/maven.yaml
---


# mvn clean

> 清理构建输出目录(target)

## 安装

```bash
同 mvn
```

## 用法

```
mvn clean
```

## 示例

### 示例 1: 清理后重新安装

```bash
mvn clean install
```

## 风险提示

> ⚠️ **HIGH**: 会删除 target 目录及其所有内容，不可恢复

## 所属维度

[[Maven-MOC|构建工具/Maven]]
