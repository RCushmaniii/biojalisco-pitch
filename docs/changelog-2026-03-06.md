# Changelog — March 6, 2026

## Summary

Added AI-powered Species Identifier feature (GPT-4o vision), deployed as a Vercel serverless function. Enhanced the data model with percentage confidence, full taxonomy, ecology, geography, conservation, and similar species. Rebuilt the Species Identifier frontend with tabbed results UI and scan history. Updated all project documentation.

---

## Species Identifier — New Feature

- **Flask backend** (`species-id/app.py`) — Accepts image uploads via camera or file, proxies to OpenAI GPT-4o vision API, returns structured species/breed data
- **Vercel serverless function** (`api/identify.py`) — Production-ready serverless version with same enhanced prompt, 1500 max tokens
- **Frontend** (`species-id/static/index.html`) — Mobile-first UI with camera capture + file upload, bilingual EN/ES toggle
- **Routing** — Updated `vercel.json` with `/api/identify` and `/species-id` routes
- **Dependencies** — Added `requirements.txt` (openai, httpx) for Vercel Python runtime

## Enhanced Data Model (v2)

- **Confidence** — Changed from high/medium/low to integer 0-100 percentage with circular gauge visualization
- **Taxonomy** — Full Kingdom through Species hierarchy with visual tree lines
- **Ecology** — Habitat, diet, size range, lifespan, behavior in 2-column card grid
- **Geography** — Native range, Jalisco/Mexico presence, invasive status with color-coded badges
- **Conservation** — IUCN status badge, population trend arrows, threats list
- **Similar species** — 1-3 species with distinguishing features
- **Domestic animals** — Breed identification with temperament, origin history, breed-specific traits

## Tabbed Results UI

- Six tabs: Overview, Taxonomy, Ecology, Range, Conservation, Similar Species
- Circular confidence gauge (green >=80%, orange >=50%, red <50%)
- Scan history stored in localStorage with tap-to-reload
- SVG icons replacing emoji throughout

## Secret Footer Link

- Leaf icon added to pitch site footer linking to `/species-id`
- Opacity: 20% base, 50% on hover
- Visible on all device sizes (no media query hiding)

## Documentation Updates

- **README.md** — Added Species Identifier section, updated project structure, badges, prerequisites, deployment instructions, results table, license (MIT -> Proprietary)
- **CLAUDE.md** — Added Species Identifier to overview, tech stack, project structure, patterns, routing, environment setup
- **portfolio.md** — Added Species Identifier outcomes, tech stack entries, tags, technical highlights

---

## Commits (chronological)

| Hash | Description |
|------|-------------|
| `4fefc3d` | feat: species identifier (GPT-4o vision) + modernized UI + secret footer link |
| `999675d` | feat: Vercel serverless species-id, improved secret footer link visibility |
| `0d0ce7e` | style: secret leaf icon opacity 20%/50% |
| `f52a070` | feat: enhanced species-id with tabbed results, confidence gauge, taxonomy, ecology, geography, conservation, scan history |
| *(staged)* | docs: update README, CLAUDE.md, portfolio.md, add changelog for March 6 |
