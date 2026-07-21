# internal/ 目录索引

> 内部实现包，不对外暴露

## 目录结构

| 子目录 | 说明 |
|--------|------|
| [`data/`](data/) | 数据加载与处理 |
| [`model/`](model/) | 数据模型定义 |
| [`service/`](service/) | 业务逻辑服务 |
| [`ui/`](ui/) | TUI 界面实现 |
| [`version/`](version/) | 版本信息管理 |

## 架构概览

```
internal/
├── data/       # YAML 数据加载、解析、索引
├── model/      # Command、Category 等结构体
├── service/    # 搜索、过滤、排序等业务逻辑
├── ui/         # Bubble Tea TUI 组件
└── version/    # 版本号、构建信息
```

## 设计原则

- 所有包均为内部使用，不导出
- 遵循 Go 项目布局标准
- 依赖注入便于测试

## 相关文件

- [`README.md`](README.md) — 详细说明
- [`../INDEX.md`](../INDEX.md) — 项目主索引