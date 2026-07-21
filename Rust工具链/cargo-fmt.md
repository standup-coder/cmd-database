---
{
  "cmd_name": "cargo fmt",
  "cmd_category": "编程语言/Rust工具链",
  "cmd_dimension": "Rust工具链",
  "cmd_install": "rustup component add rustfmt",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cargo clippy",
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

# cargo fmt

> Rust 代码格式化工具

## 安装

```bash
rustup component add rustfmt
```

## 用法

```
cargo fmt [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--` | 传递给 rustfmt 的额外选项 |
| `--check` | 仅检查格式，不修改文件 |
| `--verbose` | 显示详细输出 |

## 示例

### 示例 1: 格式化所有代码

```bash
cargo fmt
```

### 示例 2: CI 中检查格式是否正确

```bash
cargo fmt -- --check
```

### 示例 3: 仅格式化指定文件

```bash
cargo fmt -- src/main.rs
```

## 关联命令

- [[cargo-clippy]]
- [[cargo]]

## 所属维度

[[Rust工具链-MOC|编程语言/Rust工具链]]
