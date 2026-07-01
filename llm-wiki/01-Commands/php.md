---
{
  "cmd_name": "php",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "包管理器安装，如 sudo apt install php-cli",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "composer",
    "phpunit"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/more.yaml"
}
---

# php

> PHP 命令行解释器

## 安装

```bash
包管理器安装，如 sudo apt install php-cli
```

## 用法

```
php [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-r` | 运行代码 |
| `-f` | 文件 |
| `-S` | 内置服务器 |
| `-l` | 语法检查 |

## 示例

### 示例 1: 查看 PHP 版本

```bash
php -r 'echo phpversion();'
```

### 示例 2: 启动开发服务器

```bash
php -S localhost:8000
```

## 关联命令

- [[composer]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
