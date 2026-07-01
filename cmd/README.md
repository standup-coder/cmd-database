# cmd/

> cmd4coder 的命令行入口目录。

## 目录结构

```
cmd/
├── cli/        # 主 CLI 程序
│   ├── main.go          # 程序入口
│   ├── commands.go      # Cobra 子命令实现
│   ├── commands_test.go # 命令测试
│   └── main_test.go     # 入口测试
└── validator/  # YAML 数据验证工具
    ├── main.go          # 验证器入口
    └── main_test.go     # 验证器测试
```

## cli

主命令行工具，提供分类浏览、搜索、详情查看和 TUI 交互模式。

```bash
# 列出所有分类
go run ./cmd/cli categories -d ./data

# 模糊搜索命令
go run ./cmd/cli search "docker" -d ./data

# 查看单条命令详情
go run ./cmd/cli show deepspeed -d ./data

# 启动 TUI
go run ./cmd/cli -d ./data
```

## validator

验证 `data/*.yaml` 的数据格式、必填字段和分类一致性。

```bash
# 验证数据
go run ./cmd/validator -d ./data -v

# 运行测试
go test ./cmd/validator/...
```

## 构建

```bash
# 构建主二进制
go build -o bin/cmd4coder ./cmd/cli

# 交叉编译（参考 scripts/build/build.sh）
bash scripts/build/build.sh
```
