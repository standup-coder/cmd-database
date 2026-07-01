---
name: "llm-wiki-lint"
description: "Lint the LLM-Wiki vault for broken wikilinks, missing frontmatter, orphaned pages, and tag inconsistencies."
version: "1.0.0"
---

# LLM-Wiki Lint Skill

## Purpose

Maintain wiki quality by detecting and reporting structural issues.

## Checks

1. **Broken Wikilinks**
   - Scan all `[[...]]` references
   - Report links to non-existent pages
   - Suggest creating missing pages or fixing typos

2. **Missing Frontmatter**
   - Pages without YAML frontmatter
   - Required fields: `cmd_name` or `moc_type` or `scene_name`

3. **Orphaned Pages**
   - Pages with no incoming wikilinks
   - Pages not linked from any MOC

4. **Tag Audit**
   - Tags not in `_meta/taxonomy.md`
   - Inconsistent tag casing
   - Empty tag lists

5. **Duplicate Pages**
   - Multiple pages with same `cmd_name`
   - Case-insensitive name collisions

## Fix Actions

- Auto-create stub pages for broken links
- Add missing pages to appropriate MOC
- Normalize tag casing
- Report orphans for manual review
