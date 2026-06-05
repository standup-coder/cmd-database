---
cmd_name: make install
cmd_category: 构建工具/Make
cmd_dimension: Make
cmd_install: ''
cmd_platforms:
- linux
- darwin
summary: "安装已编译的程序到系统目录（通常为 /usr/local）"
cmd_level: advanced
cmd_related: []
cmd_tags:
- advanced
- linux
cmd_risk_level: high
created: '2026-05-31'
source_file: data/build/make.yaml
---


# make install

> 安装已编译的程序到系统目录（通常为 /usr/local）

## 用法

```
make install
```

```
make install PREFIX=/opt
```

## 示例

### 示例 1: 安装到默认目录 /usr/local

```bash
make install
```

### 示例 2: 安装到自定义目录

```bash
make install PREFIX=/opt/myapp
```

### 示例 3: 以 root 权限安装

```bash
sudo make install
```

## 风险提示

> ⚠️ **HIGH**: 需要 root 权限，可能覆盖系统文件

## 所属维度

[[Make-MOC|构建工具/Make]]
