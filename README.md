# Vinodh Kumar Poomari — Portfolio

A single-page, terminal-styled portfolio site for **Vinodh Kumar Poomari** (Enterprise Program Delivery Leader), built as a fully static site — no build step, no dependencies.

## Structure

```
├── index.html                              # The entire site (HTML + CSS + JS inline)
└── assets/
    └── Vinodh_Kumar_Poomari_Resume.pdf     # Served by the "Download Resume" button
```

## Sections

1. **Hero** — typed terminal effect + live "career status" dashboard card
2. **01 // About** — career story + stat grid
3. **02 // Experience** — career timeline (6 roles)
4. **03 // Skills** — technical toolkit grid
5. **04 // Highlights** — signature programs & wins
6. **05 // Education** — degrees + certification
7. **06 // Contact** — email, LinkedIn, phone

## Deploy to Vercel

### Option A — Vercel Dashboard (GitHub)
1. Push this folder to a GitHub repository.
2. Go to [vercel.com/new](https://vercel.com/new), import the repo.
3. Framework preset: **Other** (auto-detected as static). Leave all defaults.
4. Click **Deploy**.

### Option B — Vercel CLI
```bash
npm i -g vercel
cd vinodh-resume
vercel          # preview
vercel --prod   # production
```

### Option C — Drag & drop
1. Go to [vercel.com/new](https://vercel.com/new).
2. Drag the `vinodh-resume` folder onto the page.

## Customizing

All content lives directly in `index.html`. To update skills, timeline entries or highlights, edit the corresponding `<section>` — the markup is semantic and each block is clearly commented by section order.
