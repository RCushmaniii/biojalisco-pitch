# CLAUDE.md — BioJalisco Pitch Site

## Project Overview
Bilingual (ES/EN) scrollytelling single-file HTML site presenting the BioJalisco citizen-science biodiversity platform vision for western Mexico. This is a persuasion/pitch site, not the platform itself. All images are embedded as base64 data URIs for a fully self-contained deployment.

## Tech Stack
- Single-file HTML/CSS/JS (no build step, no dependencies)
- Google Fonts (Playfair Display, Source Sans 3, Cormorant Garamond)
- Intersection Observer API for scroll-triggered reveal animations
- Web Audio API for ambient forest soundscape
- Vercel for static hosting

## Project Structure
```
atlas-biodiversidad-pitch/
├── index.html          ← The entire site (single file, ~1.8MB with embedded images)
├── assets/
│   └── images/         ← Source WebP images (originals, not used at runtime)
├── docs/
│   └── PORTFOLIO.MD    ← CushLabs portfolio entry (when ready)
├── README.md
├── LICENSE
├── CLAUDE.md
├── portfolio.md
└── vercel.json         ← Vercel static site config
```

## Development Commands
```powershell
# No build step — open directly in browser
start index.html

# Or serve locally with any static server
npx serve .

# Deploy to Vercel
vercel --prod
```

## Key Patterns & Conventions
- **Bilingual system**: `data-lang="es|en"` attribute on `<body>`, `.lang-es` / `.lang-en` CSS classes hide/show content
- **Scroll reveals**: Elements with `.reveal`, `.reveal-left`, `.reveal-right`, `.reveal-scale` classes are observed by IntersectionObserver
- **Images**: All embedded as base64 data URIs in inline CSS `background-image` or `<img src>` attributes
- **Audio**: Web Audio API generates procedural forest ambience (wind noise, bird chirps, drone) — no audio files
- **5-act narrative**: Hero → Problem → Vision → Evidence → Ask

## Current Focus
Site is deployed and functional. May need iteration on copy, image swaps, or additional sections based on stakeholder feedback.

## Known Issues
- Large single-file size (~1.8MB) due to embedded base64 images — acceptable for this use case
- `background-attachment: fixed` parallax doesn't work on iOS Safari (degrades gracefully)
- Ambient audio requires user interaction to start (browser autoplay policy)

## Environment Setup
No environment variables needed. Static site with no backend.
