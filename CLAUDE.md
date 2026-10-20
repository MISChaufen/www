# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

MISChaufen team/hackerspace site for `mischaufen.de`. Pure static HTML+CSS, no build step. Target deployment: Hetzner VPS with nginx. The `CNAME` file maps GitHub Pages to `mischaufen.de` (current fallback host).

## Stack

- Pure static HTML + CSS only — no JS, no framework, no package manager
- 5 switchable themes (v1–v5) via `?style=vX` query param + `style` cookie
- `style.css` is a symlink to `style-v4.css` (production default)
- All assets self-hosted (no CDN or external dependencies)

## Theme system

JS-free switching: `serve.py` (dev) and `nginx-theme.conf` (prod) rewrite `href="style.css"` → `href="style-vX.css"` on each HTML response. Themes:

- `style-v1.css` — clean warm beige (light/dark mode via `prefers-color-scheme`)
- `style-v2.css` — warez/scene (matrix green, CRT scanlines, monospace)
- `style-v3.css` — Cyberpunk 2077 (yellow glow, angular clip-path, glitch animations)
- `style-v4.css` — raw.ag dark navy (default)
- `style-v5.css` — TRON: Legacy (deep blue-black, electric cyan, grid horizon, vignette)

All 5 themes share a scrolling hardware ticker (`animation: ticker 60s linear infinite`) in the header.

## Structure

- `index.html` — single page: About, Projects, Team, Contact; English Legal Notice + Privacy Policy in `<details>` footer elements
- `img/` — `mischaufen.jpg` + `mischaufen.webp` (hero, 640×640), `mischaufen-badge.jpg` (512×512), `webm.png` (obfuscated email)
- `favicon.ico` / `favicon.png` — 32×32 generated from badge image
- `serve.py` — dev server: 304 cache fix, cookie-based theme switching, bind 0.0.0.0:8000
- `nginx-theme.conf` — `map{}` + `sub_filter` fragments for production nginx
- `nginx-site.conf` — complete nginx server config for Hetzner deployment
- `404.html` — standalone error page (inline CSS, no external deps)
- `.github/workflows/deploy.yml` — CI/CD (to be created when server is provisioned)
