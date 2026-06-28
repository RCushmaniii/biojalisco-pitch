# Session Log — biojalisco-pitch

Entries are newest-first. Each entry documents one Claude Code working session.

---

<!-- New entries go above this line -->

## Session: 2026-06-27 (later session)

### Accomplished

- Unified the BioJalisco pitch portfolio title across all sources — it was rendering FOUR different strings (card "BioJalisco — Biodiversity Atlas Pitch Site + Species Identifier", detail headline "BioJalisco Pitch Site", generated `title` "Scrollytelling Pitch Site — BioJalisco Biodiversity Vision", ES card "Atlas de Biodiversidad e Identificador de Especies")
- Canonical now: EN "BioJalisco — Cinematic Scrollytelling Pitch Site", ES "BioJalisco — Sitio de Presentación Cinematográfico"
- biojalisco-pitch: set source `PORTFOLIO.md:10` title (PR #14, squash-merged; portfolio.md excluded from Vercel build so no deploy spent)
- cushlabs: updated `projects.generated.json`, `skills.generated.json`, `projectCardsEs.ts`, `projectDetails.ts` (EN+ES headlines), `es/projects/[slug].astro` ES SEO title (PR #132, squash-merged → production deploy Ready, verified live on detail page)
- Fixed factual error in cushlabs EN+ES SEO meta descriptions claiming the site was "Built with Next.js" — corrected to self-contained HTML5 (this project has zero Next.js)

### Decisions Made

- Title word order: brand-first ("BioJalisco — Cinematic Scrollytelling…") over technique-first, per Robert's pick — fixes the awkward grammar of his initial "Scrollytelling Cinematic for BioJalisco pitch" while keeping the cinematic-scrollytelling skill signal
- EN card/detail/SEO now all derive from the single generated `title`, so they can't diverge again; ES retains 3 hand-maintained overrides (aligned but structurally separate by the portfolio's existing design)
- Hand-edited the two `*.generated.json` files rather than re-running the full generation pipeline (pipeline scans all repos + GitHub API; hand-edit matches what a regen reproduces from the fixed PORTFOLIO.md source)

### Immediate Next Steps

- [ ] Eyeball the live portfolio card visually (curl couldn't confirm — list is client-hydrated): https://www.cushlabs.ai/portfolio/

### Technical Debt

- ES title still lives in 3 separate hand-maintained spots (projectCardsEs.ts, projectDetails.ts ES headline, es [slug].astro metaTitle) — true zero-drift would require folding ES overrides into generated data, a cross-project portfolio refactor out of scope here
- cushlabs PostToolUse formatter (Prettier) reformatted the generated JSON on save (compacted arrays, ~400 line cosmetic diff); next pipeline regen may produce a large reformat diff again — pre-existing, harmless

### Open Questions / Blockers

- None

---

## Session: 2026-06-27

### Accomplished

- Renamed portfolio entry from "BioJalisco — Biodiversity Atlas Pitch Site + Species Identifier" to "Scrollytelling Pitch Site — BioJalisco Biodiversity Vision" to de-collide with the separate `biojalisco-species-id` portfolio entry (PORTFOLIO.md:10, header comment, README.md H1)
- Dropped misleading "Atlas" framing from portfolio/README (no atlas product exists; this is a persuasion pitch). Left in-content "Biodiversity Atlas" narrative copy in index.html untouched — intentional aspirational naming
- Folded staged `vercel.json` rollout into commit: `$schema` + docs-only `ignoreCommand`
- Restored `/assets/audio` immutable cache-control headers in vercel.json — lost when the prior duplicate-key `headers` block was collapsed (now a valid second source entry)
- Added uppercase `PORTFOLIO.md` to the `ignoreCommand` exclude list (Vercel runs the git diff on case-sensitive Linux; lowercase-only exclude would burn deploys on portfolio edits)
- Committed all 5 outstanding files straight to main (5ba5762) and pushed

### Decisions Made

- Title leads with "Scrollytelling Pitch Site": first word now differs from the sibling Species Identifier entry, so the two no longer collide alphabetically/visually
- Left index.html `<title>`/OG tags as-is: that's the live site's own public branding, not a portfolio-catalog descriptor
- Committed direct to main (no PR): docs/config housekeeping, per user instruction

### Immediate Next Steps

- [ ] Verify the production deploy from 5ba5762 succeeded (this commit builds — it touches vercel.json)
- [ ] Confirm portfolio renderer picks up the new title (check sort order: title vs portfolio_priority)

### Technical Debt

- None

### Open Questions / Blockers

- None

---
