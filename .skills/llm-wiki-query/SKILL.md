---
name: "llm-wiki-query"
description: "Query the LLM-Wiki for answers. Supports tiered retrieval: index scan first, then page body if needed."
version: "1.0.0"
---

# LLM-Wiki Query Skill

## Purpose

Answer user questions using the LLM-Wiki as a knowledge source. Supports multi-turn conversation context.

## Retrieval Strategy

### Tier 1: Index Scan (cheap)
- Scan `00-Maps/` MOC pages for dimension match
- Scan page titles and frontmatter summaries
- Match `#tags` against query keywords

### Tier 2: Page Body (expensive)
- Open candidate command pages from Tier 1
- Read examples, parameters, risks
- Follow `[[wikilinks]]` for context

### Tier 3: Scene Context (conversation)
- If multi-turn, load the active scene page
- Follow the scene's decision tree
- Reference `04-FAQs/` for exact Q&A matches

## Query Patterns

### Pattern 1: Tool Discovery
```
User: "what tool should I use for distributed training?"
→ Tier 1: MOC "模型训练" → commands tagged #distributed
→ Tier 2: Open [[deepspeed]], [[accelerate]], [[megatron-lm]]
→ Answer: Compare and recommend
```

### Pattern 2: Command Usage
```
User: "how do I use vllm with tensor parallelism?"
→ Tier 1: Find [[vllm]] page
→ Tier 2: Read Options table, Examples section
→ Answer: Specific command with --tensor-parallel-size
```

### Pattern 3: Scenario Guidance (Multi-turn)
```
User: "I want to fine-tune a 7B model on a single 4090"
→ Tier 1: Scene match → [[单卡4090微调7B模型]]
→ Tier 2: Follow scene decision tree
→ Turn 1: Feasibility + tool recommendation
→ Turn 2: Command specifics
→ Turn 3: Troubleshooting if needed
```

### Pattern 4: Troubleshooting
```
User: "my training is getting OOM errors"
→ Tier 1: [[05-Troubleshooting/OOM显存不足.md]]
→ Tier 2: Cross-reference [[gradient-checkpointing]], [[deepspeed-offload]]
→ Answer: Diagnostic checklist + solutions
```

## Response Format

```
**Answer**: [synthesized answer]

**Sources**:
- [[command-name]] — specific usage
- [[scene-name]] — scenario context
- [[concept-name]] — background explanation

**Next Steps**:
- [ ] Try [[specific-command]]
- [ ] Read [[related-concept]] for deeper understanding
- [ ] Check [[troubleshooting-guide]] if issues arise
```
