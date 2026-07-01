---
name: "llm-wiki-status"
description: "Show the current state of the LLM-Wiki vault: page counts, link health, tag distribution, and delta since last update."
version: "1.0.0"
---

# LLM-Wiki Status Skill

## Purpose

Provide a dashboard view of the LLM-Wiki vault health and contents.

## Metrics to Report

1. **Page Counts**
   - Total pages
   - Commands: `01-Commands/`
   - Scenes: `02-Scenes/`
   - Concepts: `03-Concepts/`
   - FAQs: `04-FAQs/`
   - Troubleshooting: `05-Troubleshooting/`

2. **Link Health**
   - Total wikilinks
   - Broken links (pointing to non-existent pages)
   - Orphan pages (no incoming links)
   - Hub pages (most linked)

3. **Tag Distribution**
   - Top 20 tags by usage
   - Untagged pages
   - Tag clusters

4. **Source Tracking**
   - Sources in manifest
   - Last conversion timestamp
   - Delta: YAML files changed since last conversion

5. **Graph Insights**
   - Connected components
   - Bridge pages (removal partitions graph)
   - Longest path in knowledge graph
