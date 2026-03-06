# Changelog — March 5, 2026

## Summary

Major mobile UX overhaul, social sharing, link previews, narration updates, and licensing/portfolio infrastructure. The pitch site is now fully responsive with carousel interactions on mobile, shareable via social platforms, and protected under a proprietary license.

---

## Mobile Responsiveness & Carousels

- **Species carousel** — Cards now scroll-snap horizontally on mobile (`≤768px`) with dot indicators and swipe support. Padding tuned to `6%` to center cards properly on small screens.
- **Team carousel** — Roles grid converts to a horizontal scroll-snap carousel on mobile with 2 navigation dots. Auto-scrolls to Robert's card after 2.5s when the team section enters the viewport.
- **Team section viewport fit** — Tightened mobile spacing (section padding, card padding, image margins, dot margins) so the full first card + navigation dots are visible above the fold on a 375×812 viewport (iPhone X/11/12/13).
- **Problem section** — Condensed mobile padding and stat grid to fit comparison + stats within one screen.
- **Stat grid** — Changed from single-column to 3-column layout on mobile for compactness.

## Social & Link Previews

- **OG image & Twitter cards** — Added Open Graph and Twitter Card meta tags for rich link previews when sharing.
- **Share component** — Added footer share buttons for WhatsApp, LinkedIn, Email, and Copy Link.

## Narration & Audio

- **Spanish narration updates** — Re-recorded/updated Spanish audio for team and ask sections.
- **MP3 narration hooks** — Added infrastructure for MP3 narration file references in presentation mode.

## Documentation & Assets

- **Competitive landscape** — Removed HTML duplicate; kept `.md` as the canonical source document.
- **Proprietary license** — Replaced open-source license with a proprietary CushLabs license.
- **Portfolio assets** — Added portfolio-related assets and configuration.
- **Robert's photo** — New `the husband.webp` (1024×1536, quality 82) replacing the previous team photo.

## Bug Fixes

- **PDF download** — Added `/docs/` route to Vercel config so hosted PDFs resolve correctly.
- **Accessibility & timing** — Fixed `scaleRoadmap` animation timing, improved accessibility attributes.

---

## Commits (chronological)

| Hash | Description |
|------|-------------|
| `09ff209` | Fix PDF download: add /docs/ route to Vercel config |
| `32130d5` | Add OG image and Twitter card meta tags for link previews |
| `f94a998` | Add share component to footer (WhatsApp, LinkedIn, Email, Copy Link) |
| `ca1aa12` | fix: accessibility, mobile responsiveness, scaleRoadmap timing; add competitive landscape doc |
| `fd3ab5e` | docs: remove html version of competitive landscape, keep .md as source |
| `e8f81c1` | update Spanish audio narration for team and ask sections |
| `d9e3d32` | feat: mobile species carousel, MP3 narration hooks, portfolio assets, proprietary license |
| `6765e61` | feat: team carousel on mobile, species centering fix, new Robert photo |
| *(staged)* | fix: mobile team section viewport fit — dots visible above fold |
