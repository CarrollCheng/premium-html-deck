# Premium HTML Deck Design System

## Visual direction
Create a premium product keynote feel rather than a generic web page.

Recommended default system:
- Canvas: 16:9 card centered in full viewport.
- Background: deep navy / black gradient with radial glows.
- Slide surface: dark translucent panel with rounded corners and subtle border.
- Accent colors: electric blue, violet, cyan, green, orange.
- Cards: glass-like panels with 1px translucent borders and soft shadows.
- Type: large confident titles, concise body copy, strong numeric labels.

## CSS foundations
Use these values as a starting point, adapting as needed.

```css
:root{
  --bg:#070b15;
  --panel:#0d1424;
  --panel2:#111a2e;
  --ink:#f8fafc;
  --muted:#94a3b8;
  --soft:#cbd5e1;
  --line:rgba(255,255,255,.10);
  --blue:#4f8cff;
  --cyan:#22d3ee;
  --violet:#8b5cf6;
  --green:#34d399;
  --orange:#fb923c;
  --shadow:0 32px 80px rgba(0,0,0,.42);
}
html,body{
  height:100%;margin:0;overflow:hidden;color:var(--ink);
  background:radial-gradient(circle at 20% 10%,rgba(79,140,255,.18),transparent 32%),
             radial-gradient(circle at 86% 18%,rgba(139,92,246,.18),transparent 30%),
             linear-gradient(135deg,#050814,#0b1020 55%,#07111c);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","Segoe UI","PingFang SC","Microsoft YaHei",Arial,sans-serif;
}
.deck{height:100vh;width:100vw;display:flex;align-items:center;justify-content:center;padding:24px;}
.slide{width:min(94vw,1440px);aspect-ratio:16/9;display:none;position:relative;overflow:hidden;border-radius:28px;background:linear-gradient(145deg,rgba(18,27,48,.98),rgba(7,11,21,.98));box-shadow:var(--shadow);border:1px solid rgba(255,255,255,.12);padding:54px 64px;}
.slide.active{display:block;}
h1{font-size:72px;line-height:.98;letter-spacing:-.06em;margin:24px 0 18px;font-weight:950;}
h2{font-size:44px;line-height:1.05;letter-spacing:-.04em;margin:0;font-weight:950;}
.lead{font-size:22px;line-height:1.55;color:var(--soft);max-width:780px;}
.card{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.04));border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 18px 48px rgba(0,0,0,.18);}
```

## Layout patterns

### Hero layout
- Big title left.
- Floating chips or cards on the right.
- Use a strong one-sentence promise at the bottom.

### Map layout
- Use two large panels side by side.
- Each panel contains 4-6 rows.
- Use category colors, not random colors.

### Deep-dive layout
- Header: number + item name + one-line positioning.
- Body: three cards in a row: "解决什么", "典型输入", "主要产出".
- Bottom: emphasized value line.

### Workflow layout
- Use four stacked scenario cards.
- Each row: scenario label, sequence of pills, concise outcome.
- Make the final outcome pill accent-colored.

## Projection rules
- Minimum body text around 18px; important card text 20px+.
- Avoid more than 35-45 Chinese characters per paragraph line.
- Avoid dense bullet lists. Convert to cards or chips.
- Use strong contrast and large spacing.
- Keep footer and navigation small but usable.

## Interaction
Include:
- Previous / next buttons.
- Current slide counter.
- Bottom progress bar.
- Keyboard support: ArrowRight, PageDown, Space for next; ArrowLeft, PageUp for previous.

## Print / export
Use:
```css
@media print{
  body{overflow:visible;background:white;}
  .deck{display:block;width:auto;height:auto;padding:0;}
  .slide{display:block;break-after:page;box-shadow:none;width:100vw;height:100vh;aspect-ratio:auto;border-radius:0;}
  .nav,.progress,.hint{display:none;}
}
```
