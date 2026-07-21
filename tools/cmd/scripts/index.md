# scripts/ 目录索引

> 构建、数据维护和 Wiki 转换脚本

## 目录结构

| 子目录 | 说明 |
|--------|------|
| [`build/`](build/) | 构建相关脚本 |
| [`data/`](data/) | 数据维护脚本 |
| [`legacy/`](legacy/) | 旧版脚本（保留） |
| [`wiki/`](wiki/) | Wiki 转换与维护 |

## 常用脚本

### Wiki 相关

```bash
# YAML 转 Wiki
python3 scripts/wiki/convert_to_wiki.py

# Wiki 健康检查
python3 scripts/wiki/wiki_status.py
```

### 数据维护

```bash
# 数据验证
python3 scripts/data/validate.py

# 数据清理
python3 scripts/data/clean.py
```

## 相关文件

- [`README.md`](README.md) — 详细说明
- [`../INDEX.md`](../INDEX.md) — 项目主索引