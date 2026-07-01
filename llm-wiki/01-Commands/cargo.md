---
{
  "cmd_name": "cargo",
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
    "rustup",
    "rustc"
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

# cargo

> Rust 包管理器和构建工具

## 安装

```bash
同 rustup
```

## 用法

```
cargo [子命令] [选项]
```

## 参数

| Flag | Description |
|------|-------------|
| `--release` | 优化编译（生产模式） |
| `--target` | 指定编译目标平台 |
| `--features` | 启用指定 feature |
| `--no-default-features` | 禁用默认 features |
| `-j` | 并行编译线程数 |

## 示例

### 示例 1: 创建新项目

```bash
cargo new myproject
```

### 示例 2: Release 模式编译

```bash
cargo build --release
```

### 示例 3: 运行所有测试

```bash
cargo test
```

### 示例 4: 编译并运行

```bash
cargo run
```

### 示例 5: 添加依赖并启用 feature

```bash
cargo add serde --features derive
```

### 示例 6: 运行代码检查

```bash
cargo clippy
```

## 关联命令

- [[rustup]]
- [[rustc]]

## 所属维度

[[Rust工具链-MOC|编程语言/Rust工具链]]
