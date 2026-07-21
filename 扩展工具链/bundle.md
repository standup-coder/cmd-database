---
{
  "cmd_name": "bundle",
  "cmd_category": "编程语言/扩展工具链",
  "cmd_dimension": "扩展工具链",
  "cmd_install": "gem install bundler",
  "cmd_platforms": [
    "linux",
    "darwin"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "gem",
    "ruby"
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

# bundle

> Ruby 项目依赖管理

## 安装

```bash
gem install bundler
```

## 用法

```
bundle [OPTIONS] [ARGS]
```

## 参数

| Flag | Description |
|------|-------------|
| `install` | 安装 |
| `update` | 更新 |
| `exec` | 在 bundle 环境执行 |

## 示例

### 示例 1: 安装 Gemfile 依赖

```bash
bundle install
```

### 示例 2: 在 bundle 环境启动 Rails

```bash
bundle exec rails s
```

## 关联命令

- [[gem]]
- [[ruby]]

## 所属维度

[[扩展工具链-MOC|编程语言/扩展工具链]]
