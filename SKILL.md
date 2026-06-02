---
name: premium-html-deck
description: Create polished, presentation-style HTML slide decks for external sharing, executive briefings, product manager talks, skill/workflow introductions, and internal enablement. Use when the user asks to turn notes, outlines, documents, or rough content into a downloadable HTML presentation that feels like a premium 16:9 slide deck rather than a scrolling webpage. Especially useful for product, strategy, AI workflow, training, and team-sharing materials where visual quality, speaker-ready structure, and polished projection matter.
---

# Premium HTML Deck

## Goal
Create a downloadable single-file HTML presentation with a premium 16:9 slide-deck experience. The output should feel ready for projection: strong visual hierarchy, generous whitespace, clear story flow, and keyboard-based slide navigation.

Use this skill to turn rough notes, markdown, long-form content, uploaded decks, or user-provided outlines into polished HTML slides.

## Core principles
- Build a slide deck, not a webpage. Avoid long vertical scrolling pages unless the user explicitly asks for one.
- Optimize for projection. Use large type, high contrast, short lines, and clear sections.
- Make each slide communicate one main idea.
- Prefer 12-18 well-paced slides for a 8-15 minute share.
- Do not place internal production notes such as "10-minute version", "speaker notes", or "draft" in visible slide content unless the user requests them.
- If the user references a visual source such as "image 2", mirror its layout direction, rhythm, contrast, and composition, but do not blindly copy weak details.
- When converting an existing ugly or rough file, redesign the structure instead of only changing colors.

## Output requirements
Return a downloadable `.html` file unless the user asks for another format.

The HTML must be:
- self-contained: inline CSS and JavaScript, no external CDN dependencies;
- 16:9 slide-based: one `.slide` section per page;
- navigable: support next/previous buttons plus arrow keys and spacebar;
- projection-friendly: fixed viewport presentation with no accidental body scrolling;
- printable: include `@media print` rules so the user can export to PDF from the browser;
- responsive enough to open on laptops and large displays.

## Workflow
1. Identify the audience, objective, and sharing context from the user request.
2. Extract the key ideas and organize them into a narrative arc:
   - cover / promise
   - why it matters
   - capability map or framework
   - individual deep dives
   - workflows / application scenarios
   - recommended starting point
   - summary / call to action
3. Create a slide outline before coding internally. Keep slide count appropriate to the requested sharing depth.
4. Choose a visual system:
   - default: premium dark gradient, glass cards, electric blue / violet / cyan accents;
   - for product/PM content: use capability maps, workflow ribbons, metric cards, and skill detail cards;
   - for strategy content: use quadrant maps, comparison cards, timelines, and decision frameworks.
5. Generate the HTML file using the design standards below.
6. Validate locally that the file exists, opens as a single HTML file, and contains all slides.
7. Provide only the download link and a short note about what was created.

## Slide structure patterns
Use these patterns as building blocks. Mix them to avoid monotony.

### Cover slide
- Big title with 2-3 line subtitle.
- One compact promise statement.
- Decorative chips or orbit cards showing the main themes.

### Problem / why slide
- Left: problem statement.
- Right: before/after cards or contrast columns.
- Bottom: punchline sentence.

### Capability map slide
- Two or three grouped panels.
- Each item should have a short label and one concise explanation.

### Individual deep-dive slide
For each important item, use a consistent but polished structure:
- Title and one-line positioning.
- Three cards: solves, inputs, outputs.
- One emphasized PM/business value line.
- Optional workflow strip at the bottom.

### Workflow slide
- Use horizontal ribbons or stacked scenario cards.
- Each row should show: scenario -> ordered steps -> outcome.

### Closing slide
- Show recommended first steps.
- Include one strong summary sentence.
- Avoid filler or generic motivational language.

## Visual design standards
Use the bundled reference file `references/design-system.md` for detailed styling rules and examples.

Default look:
- background: dark radial gradients with subtle glow;
- slide cards: rounded 28px, glassmorphism panels, soft shadows;
- typography: very large titles, medium-large body, short paragraphs;
- accents: blue, violet, cyan, green, orange;
- spacing: airy, structured, not cramped;
- iconography: use CSS shapes, numbers, badges, pills, and cards instead of external image dependencies.

## Content quality rules
- Rewrite content for slides; do not paste paragraphs directly.
- Use nouns and short phrases on cards.
- Keep visible text concise, but not empty. A slide should be understandable without the presenter.
- For each tool/skill/workflow item, explain:
  - what it does;
  - what problem it solves;
  - typical input;
  - main output;
  - why it improves the user's work.
- Preserve user-specific terminology and skill names exactly unless clearly wrong.
- Remove backstage wording such as timing labels, prompt notes, or "this section will explain".

## Implementation guidance
- Prefer creating the file in `/mnt/data` with a clear descriptive filename.
- Use semantic sections: `<section class="slide">`.
- Include a small navigation control and progress bar.
- Include keyboard navigation JavaScript.
- Add `@media print` so every slide prints as a page.
- If the deck is based on an uploaded PPT/HTML, cite it in the chat response when required by file-search rules, but do not put citations inside the HTML.

## Quality checklist before delivery
- The deck has no visible internal timing labels unless requested.
- The first slide looks strong enough for external projection.
- Every slide has one obvious focal point.
- Text is readable at projector distance.
- The visual system is consistent but not repetitive.
- The file is downloadable and linked in the final response.
