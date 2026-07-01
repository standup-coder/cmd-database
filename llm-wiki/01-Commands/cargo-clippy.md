---
{
  "cmd_name": "cargo clippy",
  "cmd_category": "编程语言/Rust工具链",
  "cmd_dimension": "Rust工具链",
  "cmd_install": "rustup component add clippy",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cargo fmt",
    "cargo"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/rust.yaml"
}
---

# cargo clippy

> Rust 代码 lint 工具，检测常见错误和改进建议

## 安装

```bash
rustup component add clippy
```

## 用法

```
cargo clippy [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--` | 传递给 clippy 的额外选项 |
| `-W clippy::all` | 启用所有 clippy lint |
| `-D warnings` | 将警告视为错误 |
| `--fix` | 自动修复可修复的问题 |

## 示例

### 示例 1: 运行 clippy 检查

```bash
cargo clippy
```

### 示例 2: CI 中将警告视为错误

```bash
cargo clippy -- -D warnings
```

### 示例 3: 自动修复代码问题

```bash
cargo clippy --fix
```

## 关联命令

- [[cargo fmt]]
- [[cargo]]

## 所属维度

[[Rust工具链-MOC|编程语言/Rust工具链]]
