---
cmd_name: cmake
cmd_category: 构建工具/Make
cmd_dimension: Make
cmd_install: apt install cmake (Ubuntu) 或 brew install cmake (macOS)
cmd_platforms:
- linux
- darwin
- windows
summary: "跨平台构建系统生成器，管理 C/C++ 项目构建"
cmd_level: intermediate
cmd_related: []
cmd_tags:
- intermediate
- linux
cmd_risk_level: low
created: '2026-05-31'
source_file: data/build/make.yaml
---


# cmake

> 跨平台构建系统生成器，管理 C/C++ 项目构建

## 安装

```bash
apt install cmake (Ubuntu) 或 brew install cmake (macOS)
```

## 用法

```
cmake [选项] <源码路径>
```

```
cmake --build <构建目录>
```

```
cmake --install <构建目录>
```

## 参数

| Flag | Description |
|------|-------------|
| `-S` | 源码目录 |
| `-B` | 构建目录 |
| `-DCMAKE_BUILD_TYPE=Release` | 构建类型 |
| `-G` | 生成器（Unix Makefiles/Ninja/Visual Studio） |

## 示例

### 示例 1: 配置 Release 构建

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
```

### 示例 2: 执行构建

```bash
cmake --build build --config Release
```

### 示例 3: 安装

```bash
cmake --install build --prefix /usr/local
```

## 所属维度

[[Make-MOC|构建工具/Make]]
