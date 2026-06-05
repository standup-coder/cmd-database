---
name: "llm-wiki-setup"
description: "Initialize the LLM-Wiki Obsidian vault for cmd4coder. Sets up directory structure, templates, taxonomy, and graph config."
version: "1.0.0"
---

# LLM-Wiki Setup Skill

## Purpose

Initialize the `llm-wiki/` Obsidian vault from the cmd4coder project. This skill creates the canonical directory structure, templates, taxonomy, and Obsidian graph configuration.

## Vault Structure

```
llm-wiki/
├── .obsidian/
│   └── graph.json              # Obsidian graph view config
├── _meta/
│   ├── taxonomy.md             # Controlled tag vocabulary
│   └── manifest.json           # Source tracking manifest
├── _raw/                       # Staging area for unprocessed notes
├── 00-Maps/                    # MOC (Map of Content) index pages
├── 01-Commands/                # Command detail pages (693)
├── 02-Scenes/                  # Scenario pages for multi-turn QA
├── 03-Concepts/                # Concept explanation pages
├── 04-FAQs/                    # Q&A pairs corpus
├── 05-Troubleshooting/         # Troubleshooting guides
└── 99-Templates/               # Note templates
```

## Execution Steps

1. Ensure `llm-wiki/` directory exists with all subdirectories
2. Create `99-Templates/command-template.md`
3. Create `99-Templates/scene-template.md`
4. Create `99-Templates/faq-template.md`
5. Create `_meta/taxonomy.md` with canonical AI tag vocabulary
6. Create `.obsidian/graph.json` with color-coded groups by dimension
7. Initialize `_meta/manifest.json` with empty sources array
8. Create `00-Maps/README.md` as vault entry point

## Taxonomy (Canonical Tags)

Controlled vocabulary for `#tags` across the wiki:

- `#training` `#inference` `#deployment` `#evaluation` `#safety`
- `#distributed` `#quantization` `#peft` `#rlhf` `#rag`
- `#agent` `#multimodal` `#compiler` `#edge` `#federated`
- `#gpu` `#cpu` `#tpu` `#npu` `#cuda`
- `#python` `#go` `#rust` `#cpp` `#javascript`
- `#open-source` `#commercial` `#cloud` `#on-premise`
- `#beginner` `#intermediate` `#advanced` `#expert`
