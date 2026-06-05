---
cmd_name: mvn
cmd_category: 构建工具/Maven
cmd_dimension: Maven
cmd_install: sdk install maven (macOS) 或 apt install maven (Ubuntu)
cmd_platforms:
- linux
- darwin
- windows
summary: "Apache Maven 项目管理工具，用于构建和管理 Java 项目"
cmd_level: advanced
cmd_related:
- gradle
- make
cmd_tags:
- advanced
- linux
cmd_risk_level: medium
created: '2026-05-31'
source_file: data/build/maven.yaml
---


# mvn

> Apache Maven 项目管理工具，用于构建和管理 Java 项目

## 安装

```bash
sdk install maven (macOS) 或 apt install maven (Ubuntu)
```

## 用法

```
mvn [选项] [阶段]
```

```
mvn [阶段1] [阶段2] ... [阶段N]
```

## 参数

| Flag | Description |
|------|-------------|
| `-f` | 指定 POM 文件路径 |
| `-pl` | 指定构建的模块 |
| `-am` | 同时构建依赖模块 |
| `-DskipTests` | 跳过测试 |
| `-o` | 指定输出目录 |
| `-U` | 强制更新快照版本 |

## 示例

### 示例 1: 清理并安装到本地仓库

```bash
mvn clean install
```

### 示例 2: 打包跳过测试

```bash
mvn clean package -DskipTests
```

### 示例 3: 查看依赖树

```bash
mvn dependency:tree
```

### 示例 4: 从原型生成新项目

```bash
mvn archetype:generate -DgroupId=com.example -DartifactId=my-app
```

## 关联命令

- [[gradle]]
- [[make]]

## 风险提示

> ⚠️ **MEDIUM**: clean 会删除 target 目录，操作不可逆

## 所属维度

[[Maven-MOC|构建工具/Maven]]
