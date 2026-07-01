---
{
  "cmd_name": "ruby",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "包管理器安装或 rbenv",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gem",
    "bundle"
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

# ruby

> Ruby 解释器

## 安装

```bash
包管理器安装或 rbenv
```

## 用法

```
ruby [OPTIONS] [FILE]
```

## 参数

| Flag | Description |
|------|-------------|
| `-e` | 执行代码 |
| `-v` | 版本 |
| `-I` | 加载路径 |

## 示例

### 示例 1: 查看 Ruby 版本

```bash
ruby -e 'puts RUBY_VERSION'
```

### 示例 2: 运行脚本

```bash
ruby script.rb
```

## 关联命令

- [[gem]]
- [[bundle]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
