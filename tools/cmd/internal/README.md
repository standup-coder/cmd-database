# internal/

> cmd4coder 的内部 Go 包，按 Clean Architecture 分层组织。

## 目录结构

```
internal/
├── model/      # 数据模型
│   ├── command.go       # 命令实体定义
│   ├── category.go      # 分类实体定义
│   ├── config.go        # 配置模型
│   └── errors.go        # 领域错误
├── data/       # 数据加载与索引
│   ├── loader.go        # YAML 加载器
│   ├── cache.go         # 内存缓存
│   └── index.go         # 搜索索引
├── service/    # 业务逻辑层
│   ├── command_service.go  # 命令查询服务
│   ├── config.go           # 配置服务
│   └── bench_test.go       # 性能基准
├── ui/         # 用户界面
│   └── tui/
│       ├── model.go       # Bubbletea 模型
│       ├── update.go      # 消息更新逻辑
│       └── tui.go         # TUI 启动
└── version/    # 版本信息
    └── version.go
```

## 各包职责

| 包 | 职责 |
|----|------|
| `model` | 定义命令、分类、配置等核心结构体 |
| `data` | 读取 `data/*.yaml`，构建索引和缓存 |
| `service` | 对外提供查询、搜索、配置解析能力 |
| `ui/tui` | 基于 Bubbletea 的交互式终端界面 |
| `version` | 编译时注入的版本与构建信息 |

## 测试

```bash
# 运行内部包测试
go test ./internal/...

# 运行性能基准
go test -bench=. ./internal/service/...
go test -bench=. ./internal/data/...
```
