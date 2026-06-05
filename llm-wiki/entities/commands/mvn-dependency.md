---
cmd_name: mvn dependency
cmd_category: 构建工具/Maven
cmd_dimension: Maven
cmd_install: 同 mvn
cmd_platforms:
- linux
- darwin
- windows
summary: "Maven 依赖管理子命令"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/build/maven.yaml
---


# mvn dependency

> Maven 依赖管理子命令

## 安装

```bash
同 mvn
```

## 用法

```
mvn dependency:tree
```

```
mvn dependency:resolve
```

```
mvn dependency:analyze
```

## 示例

### 示例 1: 查看完整依赖树

```bash
mvn dependency:tree -Dverbose
```

## 所属维度

[[Maven-MOC|构建工具/Maven]]
