# Session Log — biojalisco-pitch

Entries are newest-first. Each entry documents one Claude Code working session.

---

<!-- New entries go above this line -->

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
