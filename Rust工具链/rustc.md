---
{
  "cmd_name": "rustc",
  "cmd_category": "编程语言/Rust工具链",
  "cmd_dimension": "Rust工具链",
  "cmd_install": "同 rustup",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cargo",
    "rustup"
  ],
  "cmd_tags": [
    "compiler",
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "low",
  "created": "2026-05-31",
  "source_file": "data/lang/rust.yaml"
}
---

# rustc

> Rust 编译器

## 安装

```bash
同 rustup
```

## 用法

```
rustc [选项] <源文件>
```

## 参数

| Flag | Description |
|------|-------------|
| `-O` | 优化编译 |
| `--edition` | 指定 Rust Edition (2015/2018/2021/2024) |
| `--emit` | 指定输出类型 (asm/ir/llvm-bc/obj/mir) |
| `-A` | 允许指定 lint |
| `-D` | 将指定 lint 视为错误 |

## 示例

### 示例 1: 编译 Rust 源文件

```bash
rustc main.rs
```

### 示例 2: 优化编译并指定输出

```bash
rustc -O main.rs -o myapp
```

### 示例 3: 使用 Rust 2021 Edition

```bash
rustc --edition 2021 main.rs
```

## 关联命令

- [[cargo]]
- [[rustup]]

## 所属维度

[[Rust工具链-MOC|编程语言/Rust工具链]]
