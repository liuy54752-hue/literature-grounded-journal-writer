---
name: literature-grounded-journal-writer
description: Draft source-grounded journal article manuscripts from user-provided target topics, outlines, research questions, variable relationships, theory notes, journal requirements, and uploaded academic literature. Use when Codex needs to read specified papers, extract original evidence and reusable writing material, synthesize literature logically, build section-level argument chains, develop introductions, literature reviews, theory/background sections, hypotheses, discussions, conclusions, or full journal-style drafts while preventing fabricated citations, page numbers, DOIs, authors, years, and source claims.
---

# Literature-Grounded Journal Writer

Use this skill to turn a target article idea and uploaded literature into a source-grounded journal manuscript. First build evidence and argument structures; then draft. Do not treat the outline as a sentence-matching form.

## Core Workflow

1. Diagnose the target article.
   - Identify the title/topic, research question, constructs, variable relationships, theory, target journal or discipline, article type, and requested language.
   - Convert rough ideas into a working outline when needed.
   - Define each section's function: problem framing, concept definition, research stream synthesis, gap construction, mechanism explanation, hypothesis derivation, discussion, or conclusion.

2. Read the specified literature.
   - Use only user-provided papers unless the user explicitly asks for external literature.
   - Extract each paper's topic, theory, research question, concepts, variables, methods, article structure, argument flow, hypotheses, findings, limitations, and transferable writing patterns.
   - Preserve source anchors whenever available: author, year, title, page, section heading, DOI, table/figure, and quoted text location.

3. Build a literature material bank.
   - Do not require every extracted sentence to directly match the target outline.
   - Classify material by rhetorical and theoretical function: background, concept definition, theoretical premise, mechanism, variable relation, research gap, debate, empirical precedent, method pattern, hypothesis wording, discussion move, or conclusion move.
   - Mark whether each item is suitable for direct short quotation, academic paraphrase, synthesis, theory-reasoning support, or structure reference.

4. Build section-level argument chains.
   - Select and combine materials based on the target topic and the section's writing task.
   - Use comparison, progression, contrast, tension, convergence, and mechanism reasoning to connect sources.
   - For literature review and hypothesis sections, explicitly show the reasoning path from prior literature to the target article's claims.

5. Draft the manuscript.
   - Draft introductions with: context -> problem -> gap -> contribution -> article roadmap.
   - Draft literature reviews with: concept definition -> research streams -> established findings -> unresolved issue -> target article positioning.
   - Draft hypotheses with: theoretical premise -> mechanism -> supporting evidence -> variable relationship -> formal hypothesis.
   - Draft discussion/conclusion sections by linking findings or expected contributions back to theory, literature, practice, limitations, and future research.

6. Audit citation integrity.
   - Never invent authors, years, page numbers, DOIs, titles, findings, or source claims.
   - Mark unavailable information as "not confirmed in provided materials."
   - Keep original excerpts, paraphrases, synthesized claims, and the author's own reasoning visibly distinct during drafting and review.

## Required Outputs

For full manuscript tasks, produce these artifacts unless the user asks for a narrower output:

- Target article structure diagnosis
- Literature reading matrix
- Literature material bank
- Original excerpt table with source anchors
- Section-level argument chains
- Section-level material combination plan
- Introduction materials and draft
- Literature review materials and draft
- Hypothesis development materials and draft
- Discussion and conclusion writing plan
- Full journal-style manuscript draft
- Citation integrity checklist

For partial tasks, produce only the relevant subset and keep the same source-grounding rules.

## Source Use Rules

- Prefer academic paraphrase, synthesis, and logical reconstruction over direct quotation.
- Use direct quotation only for short, essential wording whose original phrasing matters.
- Do not mechanically stitch together extracted sentences.
- If evidence is insufficient for a claim, state the evidence gap instead of writing with false certainty.
- When a section requires reasoning beyond a single source, explicitly combine sources into a logical chain rather than listing papers one by one.
- Keep all claims traceable to uploaded literature or clearly label them as the author's inference.

## References

Load only the reference files needed for the task:

- `references/journal-article-structure.md`: section functions and common journal article moves.
- `references/literature-synthesis-patterns.md`: synthesis, theoretical reasoning, and hypothesis development patterns.
- `references/evidence-matrix-template.md`: tables for material banks, excerpts, and argument chains.
- `references/citation-integrity.md`: rules for quotation, paraphrase, citation checking, and anti-fabrication.

## Scripts

Use scripts when they help inspect or audit source material:

- `scripts/extract_pdf_text.py`: extract PDF text with page labels when local PDF parsing dependencies are available.
- `scripts/check_citation_consistency.py`: compare in-text citations with a plain-text reference list and report mismatches.

Scripts are helpers only. Do not outsource scholarly judgment, literature synthesis, or manuscript drafting to scripts.
