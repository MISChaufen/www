# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

MISChaufen team/hackerspace site for `mischaufen.de`. Pure static HTML+CSS, no build step — deploy by copying files to the web root (or pushing to `gh-pages` for GitHub Pages). The `CNAME` file maps GitHub Pages to `mischaufen.de`.

## Stack

- Pure static HTML + CSS only — no JS, no framework, no package manager
- CSS design system adapted from benni.tech (`style.css`): warm beige background, heavy uppercase headings, cyan accent (`--accent`), full dark-mode support via `prefers-color-scheme`
- All assets self-hosted (no CDN or external dependencies)

## Structure

- `index.html` — single page with sections: About, Projects, Team, Contact; German Impressum and Datenschutzerklärung in `<details>` elements in the footer
- `style.css` — all styles; CSS custom properties in `:root` for easy theming
- `img/` — `mischaufen.jpg` (hero, 640×640), `mischaufen-badge.jpg` (header logo, 512×512), `webm.png` (obfuscated email in Impressum)
- `resume.sh` — convenience script to resume the Claude Code session
