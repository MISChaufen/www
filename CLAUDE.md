# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

MISChaufen team/hackerspace site for `mischaufen.de`. Pure static HTML+CSS, no build step. Target deployment: Hetzner VPS with nginx. The `CNAME` file maps GitHub Pages to `mischaufen.de` (current fallback host).

## Stack

- Pure static HTML + CSS only — no JS, no framework, no package manager
- 2 switchable themes (v3, v5) via `?style=vX` query param + `style` cookie
- `style.css` is a symlink to `style-v3.css` (production default)
- All assets self-hosted (no CDN or external dependencies)

## Theme system

JS-free switching: `serve.py` (dev) and `nginx-theme.conf` (prod) rewrite `href="style.css"` → `href="style-vX.css"` on each HTML response. Themes:

- `style-v3.css` — Cyberpunk 2077 (yellow glow, angular clip-path, glitch animations) **[default]**
- `style-v5.css` — TRON: Legacy (deep blue-black, electric cyan, grid horizon, vignette)

Both themes share a scrolling hardware ticker (`animation: ticker 60s linear infinite`) in the header.

## Structure

- `public/` — web server root (nginx `root` and `serve.py` point here)
  - `index.html` — single page: About, Projects, Team, Contact; Legal Notice + Privacy Policy in `<details>` footer
  - `404.html` — standalone error page (inline CSS, no external deps)
  - `favicon.ico` / `favicon.png` — 32×32
  - `style.css` — symlink → `style-v3.css`
  - `style-v3.css`, `style-v5.css` — themes
  - `img/` — `mischaufen.jpg` + `mischaufen.webp` (hero, 640×640), `mischaufen-badge.jpg`, `webm.png`
  - `CNAME` — GitHub Pages fallback mapping
- `server/` — not served; deployment and dev tooling only
  - `serve.py` — dev server: 304 cache fix, cookie-based theme switching, bind 0.0.0.0:8000
  - `serve.sh` — dev launcher shortcut
  - `nginx-site.conf` — complete nginx config for Hetzner (`root /var/www/mischaufen/public`)
  - `nginx-theme.conf` — `map{}` + `sub_filter` fragments for production nginx
- `docs/` — not served; legal research and compliance notes
- `.github/workflows/deploy.yml` — CI/CD (to be created when server is provisioned)
