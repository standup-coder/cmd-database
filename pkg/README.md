# pkg/

> 可复用的导出包，供 CLI 或外部项目直接使用。

## 目录结构

```
pkg/
└── export/
    ├── json.go      # 导出为 JSON
    ├── markdown.go  # 导出为 Markdown
    ├── yaml.go      # 导出为 YAML
    └── export_test.go
```

## export 包

提供命令数据到不同格式的导出能力，当前支持：

- **JSON**：机器可读格式
- **Markdown**：人类可读文档
- **YAML**：保持与数据源一致的格式

```bash
# 通过 CLI 导出示例（如已支持）
go run ./cmd/cli export -d ./data -f json -o commands.json
```

## 测试

```bash
go test ./pkg/export/...
```
