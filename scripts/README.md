# scripts/

> cmd4coder 的转换、维护与构建脚本集合。

## 目录结构

```
scripts/
├── build/      # 构建脚本
│   ├── build.sh
│   ├── build.ps1
│   └── test_core.sh
├── data/       # 数据维护脚本
│   ├── dedup_commands.py
│   ├── enrich_examples.py
│   ├── enrich_new_risks.py
│   ├── enrich_risks.py
│   ├── fix_json_frontmatter.py
│   ├── generate_commands_md.py
│   └── ingest_new_commands.py
├── wiki/       # Wiki 转换与维护脚本
│   ├── convert_to_wiki.py
│   ├── fix_wiki_links_v3.py
│   ├── generate_scenes_and_faqs.py
│   ├── wiki_status.py
│   └── ... (11 more)
└── legacy/     # 一次性批量脚本
    └── add_bulk_commands.py
```

## 常用脚本

### 构建

```bash
# 跨平台构建二进制
bash scripts/build/build.sh

# 核心测试
bash scripts/build/test_core.sh
```

### 数据维护

```bash
# 生成 COMMANDS.md
python3 scripts/data/generate_commands_md.py

# 去重
python3 scripts/data/dedup_commands.py

# 补全风险等级
python3 scripts/data/enrich_risks.py
```

### Wiki 维护

```bash
# YAML → Markdown 转换
python3 scripts/wiki/convert_to_wiki.py

# 修复 wikilinks
python3 scripts/wiki/fix_wiki_links_v3.py

# 检查 Wiki 健康
python3 scripts/wiki/wiki_status.py

# 生成场景页与 FAQ
python3 scripts/wiki/generate_scenes_and_faqs.py
```

## 注意事项

- `legacy/` 中的脚本主要用于历史批量导入，新项目维护请优先使用 `data/` 和 `wiki/` 下的脚本。
- 修改 YAML 后，建议按「验证 → 转换 → 修复链接 → 检查状态」的顺序执行。
