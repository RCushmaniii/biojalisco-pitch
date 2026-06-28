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
- Made ES title single-source: new `src/data/esCanonicalTitles.ts` exports `ES_TITLE_BIOJALISCO_PITCH`, referenced by all 3 ES surfaces (card, detail headline, SEO title) so they can't drift (cushlabs PR #133)
- Caught + fixed a 4th drift point via live verification: EN detail SEO `<title>` still rendered "BioJalisco — Biodiversity Atlas" (stale `metaTitles` override in `projects/[slug].astro` missed first pass — only EN descriptions were checked, not EN titles). Removed it so EN SEO title falls back to generated canonical title (cushlabs PR #134)
- Verified all 4 detail surfaces live (EN/ES × headline/SEO title) — all canonical, zero stale strings
- Investigated the logged "ES cards show English" debt — confirmed it is NOT debt: those are brand/product names (Unwatermark, AI Resume Tailor, CushLabs Messenger…) that intentionally mirror the EN cards per `projectCardsEs.ts` policy. No change made; item closed.
- Fixed a real defect found during that investigation: ES detail copy for ~9 projects in `projectDetails.ts` was written entirely WITHOUT accents (~300 corrections) — es-MX standard violation (cushlabs PR #136, deployed + verified live)

### Decisions Made

- Title word order: brand-first ("BioJalisco — Cinematic Scrollytelling…") over technique-first, per Robert's pick — fixes the awkward grammar of his initial "Scrollytelling Cinematic for BioJalisco pitch" while keeping the cinematic-scrollytelling skill signal
- EN now single-sources from generated `title` (card, detail headline, SEO title all derive from it); ES now single-sources from `ES_TITLE_BIOJALISCO_PITCH` const
- ES consolidated via a scoped named constant rather than changing the shared ES fallback chain — the fallback change would have altered ES card titles for ~6 other projects (mazebreak-wiki, ny-eng, cushlabs-scrollytelling, ai-resume-tailor, etc.)
- Hand-edited the two `*.generated.json` files rather than re-running the full generation pipeline (pipeline scans all repos + GitHub API; hand-edit matches what a regen reproduces from the fixed PORTFOLIO.md source)
- ES diacritics fixed with a dictionary-driven script (nspell + dictionary-es): only changed words whose unaccented form is invalid Spanish but valid once accented — complete + safe (leaves valid words, English tech terms, brands). Context homographs (ano→año, ingles→inglés, verb esta→está, mas→más, Desafio→Desafío) fixed by hand. Brands kept unaccented: Neon, Claude Vision, ingestion, manager, union. Scoped to ES-block lines only so EN copy in the same file was never touched.

### Immediate Next Steps

- [ ] Eyeball the live portfolio cards visually (curl can't — lists are client-hydrated; data sources verified canonical): https://www.cushlabs.ai/portfolio/ and https://www.cushlabs.ai/es/portfolio/

### Technical Debt

- None outstanding from this session. (The previously-logged "ES cards show English" item was investigated and closed as non-debt — brand names by design. ES detail diacritics now fixed + verified.)
- Minor/low-impact: Spanish _tilde diacrítica_ on monosyllable homographs (él/sí/mí/sé) in `projectDetails.ts` ES copy was not exhaustively reviewed — only the high-impact missing-word accents and the common homographs (esta/tú/más/aún) were corrected. No known incorrect instance; flagged for completeness.
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
