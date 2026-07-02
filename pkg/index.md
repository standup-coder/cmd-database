# pkg/ 目录索引

> 可复用的公共包

## 目录结构

| 子目录 | 说明 |
|--------|------|
| [`export/`](export/) | 数据导出功能（JSON、Markdown、YAML） |

## 功能说明

### export 包

提供多种格式的数据导出能力：

- **JSON** — 结构化数据导出
- **Markdown** — 文档格式导出
- **YAML** — 配置格式导出

## 使用示例

```go
import "cmd4coder/pkg/export"

// 导出为 JSON
export.ToJSON(commands, "output.json")

// 导出为 Markdown
export.ToMarkdown(commands, "output.md")
```

## 相关文件

- [`README.md`](README.md) — 详细说明
- [`../INDEX.md`](../INDEX.md) — 项目主索引