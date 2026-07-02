# cmd/ 目录索引

> CLI 命令行程序入口点

## 目录结构

| 子目录 | 说明 |
|--------|------|
| [`cli/`](cli/) | 主 CLI 程序，包含所有命令实现 |
| [`validator/`](validator/) | 数据验证工具 |

## 快速开始

```bash
# 构建 CLI 二进制
go build -o bin/cmd4coder ./cmd/cli

# 运行 CLI
go run ./cmd/cli -d ./data
```

## 主要功能

- 命令搜索与查询
- 分类浏览
- TUI 交互模式
- 数据导出

## 相关文件

- [`README.md`](README.md) — 详细说明
- [`../INDEX.md`](../INDEX.md) — 项目主索引