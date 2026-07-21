---
{
  "cmd_name": "rustup",
  "cmd_category": "编程语言/Rust工具链",
  "cmd_dimension": "Rust工具链",
  "cmd_install": "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
  "cmd_platforms": [
    "linux",
    "darwin",
    "windows"
  ],
  "cmd_level": "intermediate",
  "cmd_related": [
    "cargo",
    "rustc"
  ],
  "cmd_tags": [
    "intermediate",
    "linux"
  ],
  "cmd_risk_level": "medium",
  "created": "2026-05-31",
  "source_file": "data/lang/rust.yaml"
}
---

# rustup

> Rust 工具链安装器和版本管理器

## 安装

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## 用法

```
rustup [子命令]
```

## 参数

| Flag | Description |
|------|-------------|
| `update` | 更新 Rust 工具链 |
| `default` | 设置默认工具链版本 |
| `toolchain` | 管理已安装的工具链 |
| `target` | 管理交叉编译目标 |
| `component` | 管理工具链组件 (rustfmt, clippy) |

## 示例

### 示例 1: 更新 Rust 到最新稳定版

```bash
rustup update
```

### 示例 2: 切换到 nightly 工具链

```bash
rustup default nightly
```

### 示例 3: 添加 Linux musl 交叉编译目标

```bash
rustup target add x86_64-unknown-linux-musl
```

### 示例 4: 安装 clippy 和 rustfmt 组件

```bash
rustup component add clippy rustfmt
```

## 关联命令

- [[cargo]]
- [[rustc]]

## 风险提示

> ⚠️ **MEDIUM**: update 可能导致现有项目编译失败

## 所属维度

[[Rust工具链-MOC|编程语言/Rust工具链]]
