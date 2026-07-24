#!/usr/bin/env python3
"""
cmd4coder YAML → Obsidian LLM-Wiki Converter
Follows Ar9av/obsidian-wiki spec:
- YAML frontmatter
- [[wikilinks]]
- .manifest.json delta tracking
- _meta/taxonomy.md
"""

import yaml
import json
import os
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parents[4]  # repo root
CMD_ROOT = Path(__file__).resolve().parents[2]  # tools/cmd
DATA_DIR = CMD_ROOT / "data"  # YAML 单一数据源随 CLI 收敛到 tools/cmd/data
WIKI_DIR = PROJECT_ROOT / "llm-wiki"
META_DIR = WIKI_DIR / "_meta"
COMMANDS_DIR = WIKI_DIR / "01-Commands"
MAPS_DIR = WIKI_DIR / "00-Maps"
SCENES_DIR = WIKI_DIR / "02-Scenes"
CONCEPTS_DIR = WIKI_DIR / "03-Concepts"
FAQS_DIR = WIKI_DIR / "04-FAQs"
TROUBLE_DIR = WIKI_DIR / "05-Troubleshooting"
OBSIDIAN_DIR = WIKI_DIR / ".obsidian"

# Dimension mapping from category name
def extract_dimension(category: str) -> str:
    if not category:
        return "other"
    parts = category.split("/")
    if len(parts) >= 2:
        dim = parts[-1]
    else:
        dim = parts[0] if parts else "other"
    # Clean for filename
    dim = re.sub(r'[^\w\s-]', '', dim).strip()
    return dim

def slugify(name: str) -> str:
    """Convert command name to safe filename"""
    s = re.sub(r'[^\w\s-]', '', name)
    s = re.sub(r'[-\s]+', '-', s)
    return s.lower().strip('-')

def cmd_level(cmd: dict) -> str:
    """Determine beginner/intermediate/advanced from content"""
    desc = cmd.get("description", "").lower()
    name = cmd.get("name", "").lower()
    risks = cmd.get("risks", [])
    
    if any(r.get("level") == "critical" or r.get("level") == "high" for r in risks):
        return "advanced"
    if any(k in desc for k in ["分布式", "大规模", "并行", "cluster", "distributed", "production"]):
        return "advanced"
    if any(k in name for k in ["deepspeed", "megatron", "tensorrt", "triton", "mlir"]):
        return "advanced"
    if any(k in desc for k in ["简单", "入门", "quick", "easy", "初学者"]):
        return "beginner"
    return "intermediate"

def infer_tags(cmd: dict, dimension: str) -> list:
    """Infer tags from command metadata"""
    tags = []
    desc = cmd.get("description", "").lower()
    name = cmd.get("name", "").lower()
    category = cmd.get("category", "").lower()
    
    # Dimension tags
    dim_map = {
        "训练": "training", "推理": "inference", "部署": "deployment",
        "评测": "evaluation", "监控": "monitoring", "安全": "safety",
        "agent": "agent", "多模态": "multimodal", "编译器": "compiler",
        "边缘": "edge", "联邦": "federated", "可解释": "interpretability",
        "网关": "gateway", "应用": "application", "架构": "architecture",
        "rag": "rag", "数据": "data", "向量": "vector-db",
    }
    for cn, en in dim_map.items():
        if cn in category or cn in desc:
            tags.append(en)
    
    # Technique tags
    technique_keywords = {
        "lora": "peft", "qlora": "peft", "peft": "peft",
        "量化": "quantization", "quantization": "quantization", "int8": "quantization", "fp16": "quantization",
        "蒸馏": "distillation", "distill": "distillation",
        " RL": "rlhf", "PPO": "rlhf", "DPO": "rlhf", "GRPO": "rlhf",
        "docker": "docker", "kubernetes": "kubernetes", "k8s": "kubernetes",
        "gpu": "gpu", "cuda": "gpu",
        "分布式": "distributed", "parallel": "distributed",
        "微调": "fine-tuning", "fine-tune": "fine-tuning",
        "预训练": "pre-training", "pretrain": "pre-training",
    }
    for kw, tag in technique_keywords.items():
        if kw.lower() in desc or kw.lower() in name:
            if tag not in tags:
                tags.append(tag)
    
    # Level tag
    level = cmd_level(cmd)
    tags.append(level)
    
    # Platform tag
    platforms = cmd.get("platforms", [])
    if "linux" in platforms:
        tags.append("linux")
    
    # Open source vs commercial
    install = cmd.get("install_method", "")
    if "pip install" in install or "git clone" in install or "npm install" in install:
        tags.append("open-source")
    elif "docker pull" in install:
        tags.append("open-source")
    
    return tags

def generate_command_page(cmd: dict, yaml_file: str, all_cmd_names: set) -> str:
    """Generate a single command markdown page"""
    name = cmd.get("name", "unknown")
    category = cmd.get("category", "")
    dimension = extract_dimension(category)
    description = cmd.get("description", "")
    install = cmd.get("install_method", "")
    platforms = cmd.get("platforms", [])
    related = cmd.get("related_commands", [])
    risks = cmd.get("risks", [])
    refs = cmd.get("references", [])
    usage = cmd.get("usage", [])
    options = cmd.get("options", [])
    examples = cmd.get("examples", [])
    
    tags = infer_tags(cmd, dimension)
    level = cmd_level(cmd)
    
    # Related wikilinks - only link to commands that exist
    related_links = []
    for r in related:
        r_clean = r.strip()
        if r_clean in all_cmd_names:
            related_links.append(f"[[{r_clean}]]")
    
    risk_level = "low"
    risk_desc = ""
    if risks:
        risk_level = risks[0].get("level", "low")
        risk_desc = risks[0].get("description", "")
    
    # Build options table
    options_md = ""
    if options:
        options_md = "| Flag | Description |\n|------|-------------|\n"
        for opt in options:
            flag = opt.get("flag", "").replace("|", "\\|")
            desc = opt.get("description", "").replace("|", "\\|")
            options_md += f"| `{flag}` | {desc} |\n"
    
    # Build examples
    examples_md = ""
    if examples:
        for i, ex in enumerate(examples, 1):
            ex_cmd = ex.get("command", "")
            ex_desc = ex.get("description", "")
            examples_md += f"### 示例 {i}: {ex_desc}\n\n"
            examples_md += f"```bash\n{ex_cmd}\n```\n\n"
    
    # Build references
    refs_md = ""
    if refs:
        for ref in refs:
            refs_md += f"- [{ref}]({ref})\n"
    
    # Build usage
    usage_md = ""
    if usage:
        for u in usage:
            usage_md += f"```\n{u}\n```\n\n"
    
    # Frontmatter
    frontmatter = {
        "cmd_name": name,
        "cmd_category": category,
        "cmd_dimension": dimension,
        "cmd_install": install,
        "cmd_platforms": platforms,
        "cmd_level": level,
        "cmd_related": related,
        "cmd_tags": tags,
        "cmd_risk_level": risk_level,
        "created": "2026-05-31",
        "source_file": str(Path(yaml_file).relative_to(PROJECT_ROOT)),
    }
    
    fm_lines = json.dumps(frontmatter, ensure_ascii=False, indent=2)
    
    md = f"---\n{fm_lines}\n---\n\n"
    md += f"# {name}\n\n"
    md += f"> {description}\n\n"
    
    if install:
        md += "## 安装\n\n"
        md += f"```bash\n{install}\n```\n\n"
    
    if usage_md:
        md += "## 用法\n\n"
        md += usage_md
    
    if options_md:
        md += "## 参数\n\n"
        md += options_md + "\n"
    
    if examples_md:
        md += "## 示例\n\n"
        md += examples_md
    
    if related_links:
        md += "## 关联命令\n\n"
        for link in related_links:
            md += f"- {link}\n"
        md += "\n"
    
    if risk_desc:
        md += f"## 风险提示\n\n"
        md += f"> ⚠️ **{risk_level.upper()}**: {risk_desc}\n\n"
    
    if refs_md:
        md += "## 参考链接\n\n"
        md += refs_md + "\n"
    
    # Add dimension link
    md += f"## 所属维度\n\n"
    md += f"[[{dimension}-MOC|{category}]]\n"
    
    return md

def generate_moc_page(category: str, description: str, commands: list, order: int) -> str:
    """Generate a MOC (Map of Content) page for a category"""
    dimension = extract_dimension(category)
    
    frontmatter = {
        "moc_type": "dimension",
        "moc_name": category,
        "moc_order": order,
        "tags": ["MOC", "AI", dimension],
    }
    
    fm_lines = json.dumps(frontmatter, ensure_ascii=False, indent=2)
    
    md = f"---\n{fm_lines}\n---\n\n"
    md += f"# {category}\n\n"
    md += f"> {description}\n\n"
    md += "## 命令列表\n\n"
    
    for cmd in sorted(commands, key=lambda x: x.get("name", "")):
        name = cmd.get("name", "")
        desc = cmd.get("description", "")
        level = cmd_level(cmd)
        level_emoji = {"beginner": "🟢", "intermediate": "🟡", "advanced": "🔴"}.get(level, "⚪")
        md += f"- {level_emoji} [[{name}]] — {desc[:80]}{'...' if len(desc) > 80 else ''}\n"
    
    md += "\n## 统计\n\n"
    md += f"- 总命令数: {len(commands)}\n"
    md += f"- 维度: {dimension}\n"
    
    return md

def generate_readme(all_categories: list, total_commands: int) -> str:
    """Generate vault README"""
    md = "---\n"
    md += "moc_type: root\n"
    md += "tags: [\"MOC\", \"README\"]\n"
    md += "---\n\n"
    md += "# LLM-Wiki\n\n"
    md += "> cmd4coder 大模型领域知识库 — Obsidian Wiki 版\n\n"
    md += f"**统计**: {total_commands} 命令 / {len(all_categories)} 分类 / 2026-05-31 生成\n\n"
    md += "## 维度导航\n\n"
    md += "| 维度 | 分类 | 命令数 |\n"
    md += "|------|------|--------|\n"
    
    for cat_info in sorted(all_categories, key=lambda x: x["order"]):
        cat_name = cat_info["name"]
        dim = extract_dimension(cat_name)
        count = len(cat_info["commands"])
        md += f"| [[{dim}-MOC|{cat_name}]] | {dim} | {count} |\n"
    
    md += "\n## 快速入口\n\n"
    md += "- [[模型训练-MOC]] — 大模型训练与微调\n"
    md += "- [[模型推理-MOC]] — 推理部署与优化\n"
    md += "- [[Agent工程-MOC]] — AI Agent 开发\n"
    md += "- [[评测-MOC]] — 模型评测与基准\n"
    md += "- [[AI安全-MOC]] — 安全与合规\n"
    
    md += "\n## 图谱视图\n\n"
    md += "在 Obsidian 中打开 **Graph View** 查看知识关联。\n"
    md += "节点按维度着色，双向链接显示工具关联。\n"
    
    return md

def generate_taxonomy() -> str:
    """Generate taxonomy.md"""
    md = "---\n"
    md += "moc_type: meta\n"
    md += "tags: [\"meta\", \"taxonomy\"]\n"
    md += "---\n\n"
    md += "# 标签分类 (Taxonomy)\n\n"
    md += "> 控制词汇表。所有页面标签应从此列表中选择。\n\n"
    
    taxonomy = {
        "阶段": ["training", "inference", "deployment", "evaluation", "monitoring"],
        "技术": ["distributed", "quantization", "peft", "rlhf", "rag", "agent", "multimodal"],
        "基础设施": ["compiler", "edge", "federated", "gateway", "vector-db"],
        "硬件": ["gpu", "cpu", "tpu", "npu", "cuda"],
        "安全": ["safety", "privacy", "interpretability"],
        "难度": ["beginner", "intermediate", "advanced"],
        "类型": ["open-source", "commercial", "cloud", "on-premise"],
    }
    
    for group, tags in taxonomy.items():
        md += f"## {group}\n\n"
        for tag in tags:
            md += f"- `#{tag}`\n"
        md += "\n"
    
    return md

def generate_graph_json(categories: list) -> str:
    """Generate Obsidian graph.json with color coding by dimension"""
    colors = [
        {"query": "tag:MOC", "color": {"a": 1, "rgb": 14701138}},  # orange
        {"query": "tag:training", "color": {"a": 1, "rgb": 11621088}},  # blue
        {"query": "tag:inference", "color": {"a": 1, "rgb": 5395168}},  # green
        {"query": "tag:evaluation", "color": {"a": 1, "rgb": 14701233}},  # purple
        {"query": "tag:safety", "color": {"a": 1, "rgb": 14701233}},  # red
        {"query": "tag:agent", "color": {"a": 1, "rgb": 14701233}},  # yellow
        {"query": "tag:advanced", "color": {"a": 1, "rgb": 14701233}},  # dark
    ]
    
    graph = {
        "collapse-filter": True,
        "search": "",
        "showTags": True,
        "showAttachments": False,
        "hideUnresolved": False,
        "showOrphans": True,
        "collapse-color-groups": False,
        "colorGroups": colors,
        "collapse-display": True,
        "showArrow": False,
        "textFadeMultiplier": 0,
        "nodeSizeMultiplier": 1,
        "lineSizeMultiplier": 1,
        "collapse-forces": True,
        "centerStrength": 0.518713248970312,
        "repelStrength": 10,
        "linkStrength": 1,
        "linkDistance": 250,
        "scale": 0.7132754626224452,
        "close": False
    }
    
    return json.dumps(graph, indent=2)

def generate_manifest(sources: list) -> str:
    """Generate manifest.json"""
    manifest = {
        "version": "1.0.0",
        "updated_at": datetime.now().isoformat(),
        "sources": sources,
    }
    return json.dumps(manifest, indent=2, ensure_ascii=False)

def main():
    print("=" * 60)
    print("cmd4coder → LLM-Wiki Converter")
    print("=" * 60)
    
    # Ensure directories exist
    for d in [COMMANDS_DIR, MAPS_DIR, SCENES_DIR, CONCEPTS_DIR, FAQS_DIR, TROUBLE_DIR, META_DIR, OBSIDIAN_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    
    # First pass: collect all command names for link validation
    all_cmd_names = set()
    all_categories = []
    sources = []
    total_commands = 0
    
    yaml_files = list(DATA_DIR.rglob("*.yaml"))
    print(f"Found {len(yaml_files)} YAML files")
    
    # First pass: collect names
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data and "commands" in data:
                for cmd in data["commands"]:
                    name = cmd.get("name", "")
                    if name:
                        all_cmd_names.add(name)
        except Exception as e:
            print(f"Warning: failed to parse {yaml_file}: {e}")
    
    print(f"Found {len(all_cmd_names)} unique commands")
    
    # Second pass: generate pages
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            if not data or "commands" not in data:
                continue
            
            category = data.get("category", "未分类")
            description = data.get("description", "")
            commands = data.get("commands", [])
            
            if not commands:
                continue
            
            # Generate command pages
            file_cmd_names = []
            for cmd in commands:
                name = cmd.get("name", "")
                if not name:
                    continue
                
                md = generate_command_page(cmd, str(yaml_file), all_cmd_names)
                cmd_file = COMMANDS_DIR / f"{slugify(name)}.md"
                with open(cmd_file, "w", encoding="utf-8") as f:
                    f.write(md)
                
                file_cmd_names.append(name)
                total_commands += 1
            
            # Generate MOC page
            dim = extract_dimension(category)
            moc_file = MAPS_DIR / f"{dim}-MOC.md"
            # For ordering, we don't have order in yaml, use filename order
            moc_md = generate_moc_page(category, description, commands, 0)
            with open(moc_file, "w", encoding="utf-8") as f:
                f.write(moc_md)
            
            all_categories.append({
                "name": category,
                "dimension": dim,
                "commands": commands,
                "order": 0,
            })
            
            sources.append({
                "file": str(yaml_file.relative_to(PROJECT_ROOT)),
                "commands_generated": file_cmd_names,
                "mocs_generated": [category],
                "timestamp": datetime.now().isoformat(),
            })
            
            print(f"  ✓ {yaml_file.name}: {len(commands)} commands → {dim}-MOC")
            
        except Exception as e:
            print(f"  ✗ Error processing {yaml_file}: {e}")
            import traceback
            traceback.print_exc()
    
    # Generate root README
    readme_md = generate_readme(all_categories, total_commands)
    with open(MAPS_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)
    
    # Generate taxonomy
    tax_md = generate_taxonomy()
    with open(META_DIR / "taxonomy.md", "w", encoding="utf-8") as f:
        f.write(tax_md)
    
    # Generate graph.json
    graph_json = generate_graph_json(all_categories)
    with open(OBSIDIAN_DIR / "graph.json", "w", encoding="utf-8") as f:
        f.write(graph_json)
    
    # Generate manifest
    manifest_json = generate_manifest(sources)
    with open(META_DIR / "manifest.json", "w", encoding="utf-8") as f:
        f.write(manifest_json)
    
    # Generate templates
    templates_dir = WIKI_DIR / "99-Templates"
    templates_dir.mkdir(exist_ok=True)
    
    with open(templates_dir / "command-template.md", "w", encoding="utf-8") as f:
        f.write(generate_command_page({
            "name": "command-name",
            "category": "维度/分类",
            "description": "一句话描述",
            "install_method": "pip install xxx",
            "platforms": ["linux", "darwin", "windows"],
            "related_commands": ["related-cmd"],
            "risks": [{"level": "low", "description": "风险描述"}],
            "references": ["https://example.com"],
            "usage": ["command [OPTIONS]"],
            "options": [{"flag": "--flag", "description": "描述"}],
            "examples": [{"command": "cmd --flag", "description": "示例"}],
        }, str(PROJECT_ROOT / "data/example.yaml"), set()))
    
    print("\n" + "=" * 60)
    print(f"Conversion complete!")
    print(f"  Commands:   {total_commands}")
    print(f"  Categories: {len(all_categories)}")
    print(f"  Sources:    {len(sources)}")
    print(f"  Output:     {WIKI_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
