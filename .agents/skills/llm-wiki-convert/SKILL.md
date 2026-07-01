---
name: "llm-wiki-convert"
description: "Convert cmd4coder YAML data files into Obsidian Markdown wiki pages. Generates command pages, MOC indexes, and cross-links."
version: "1.0.0"
---

# LLM-Wiki Convert Skill

## Purpose

Convert cmd4coder's YAML command database into an Obsidian-compatible Markdown vault with YAML frontmatter, wikilinks, and structured content.

## Source Format

Input: `data/**/*.yaml` files, each containing:
- `category`: string
- `description`: string
- `commands`: array of command objects

## Target Format

Output: `llm-wiki/**/*.md` files with:
- YAML frontmatter (metadata)
- Markdown body with structured sections
- `[[wikilinks]]` to related commands
- `#tags` from taxonomy

## Conversion Rules

### Command Page (`01-Commands/{name}.md`)

```markdown
---
cmd_name: "{name}"
cmd_category: "{category}"
cmd_dimension: "{dimension}"
cmd_install: "{install_method}"
cmd_platforms: [{platforms}]
cmd_level: "{level}"
cmd_related: [{related}]
cmd_tags: [{tags}]
cmd_use_cases: [{use_cases}]
cmd_risk_level: "{risk_level}"
created: "2026-05-31"
source_file: "{yaml_file}"
---

# {name}

> {description}

## Installation

```bash
{install_method}
```

## Usage

```
{usage}
```

## Options

| Flag | Description |
|------|-------------|
{options_table}

## Examples

{examples}

## Related Commands

{related_wikilinks}

## Risk Level: {risk_level}

{risks}

## References

{references}
```

### MOC Page (`00-Maps/{dimension}-MOC.md`)

```markdown
---
moc_type: "dimension"
moc_name: "{category}"
moc_order: {order}
tags: ["MOC", "AI", "{dimension}"]
---

# {category}

> {description}

## Commands

{command_list}

## Related Dimensions

{related_mocs}
```

### Manifest Format (`_meta/manifest.json`)

```json
{
  "version": "1.0.0",
  "updated_at": "2026-05-31",
  "sources": [
    {
      "file": "data/ai/llm-training.yaml",
      "commands_generated": ["deepspeed", "accelerate", ...],
      "mocs_generated": ["AI基础设施/大模型训练"],
      "timestamp": "2026-05-31T10:00:00Z"
    }
  ]
}
```

## Execution Steps

1. Parse all `data/**/*.yaml` files
2. For each command, generate `01-Commands/{name}.md`
3. For each category, generate `00-Maps/{category}-MOC.md`
4. Resolve `[[wikilinks]]` between related commands
5. Generate `_meta/manifest.json`
6. Run `wiki-lint` to verify links
