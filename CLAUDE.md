# CLAUDE.md

## Project Overview

Personal website and portfolio for Frédéric Montet, built with **Quarto** (static site generator). Content is authored in `.qmd` (Quarto markdown) files with YAML frontmatter. Python code in data stories is executed via Jupyter during the build.

## Build & Run Commands

| Task | Command |
|------|---------|
| Install dependencies | `make sync` or `uv sync` |
| Preview (dev server) | `make preview` or `uv run quarto preview` |
| Full dev setup | `make dev` (sync + preview) |
| Build static site | `make build` or `uv run quarto render` |
| Production build | `make publish` (clean + build) |
| Clean artifacts | `make clean` (removes `_site/` and `.quarto/`) |
| Add Python package | `uv add package-name` |

There are no tests or linters configured.

## Project Structure

```
_quarto.yml          # Quarto site configuration (navbar, theme, execution)
pyproject.toml       # Python deps (altair, pandas, numpy, jupyter, pyyaml)
Makefile             # Build automation
theme.scss           # Custom SCSS theme (Noto fonts, CSS variables, responsive)
index.qmd            # Home page with latest stories listing
research.qmd         # Research page
stories.qmd          # Stories listing page
stories/             # Story content, one directory per story
  thought-*/index.qmd
  story-*/index.qmd
  data-story-*/index.qmd
  photographic-story-*/index.qmd
images/              # Site-wide images
_site/               # Generated output (git-ignored, never edit)
.quarto/             # Build cache (git-ignored)
```

## Key Conventions

- **Base theme**: Sandstone (set in `_quarto.yml`), with custom overrides in `theme.scss`
- **Fonts**: Noto Sans (body), Noto Serif (headings), Noto Sans Mono (code)
- **All commands run through UV**: Use `uv run` prefix or `make` targets, not bare `quarto`
- **Python >=3.11** required
- **`uv.lock`** must be committed for reproducible builds

## Story Types

Stories live in `stories/<type>-<n>/index.qmd`. Four formats:

1. **Thought** (`thought-*`) — Short tweet-like observations. Wrapped in `::: {.thought}` div. Category: `thought`.
2. **Story** (`story-*`) — Long-form narrative with blockquotes, `==highlighted text==`, sections, and references.
3. **Data Story** (`data-story-*`) — Jupyter-executable. Frontmatter includes `jupyter: python3`. Uses Altair for interactive visualizations.
4. **Photographic Story** (`photographic-story-*`) — Image-focused. Frontmatter includes `lightbox: true`. Images use groups for gallery display.

Each story directory may contain a `references.bib` for citations (`[@key]` syntax).

## Adding Content

- **New story**: Create `stories/<type>-<n>/index.qmd` with proper frontmatter (title, date, categories). Add `references.bib` if needed.
- **New page**: Create `.qmd` file at root, add to `website.navbar.left` in `_quarto.yml`.

## Things to Avoid

- Never edit files in `_site/` — they are generated
- Never edit `.quarto/` cache files
- Don't add unnecessary dependencies or tooling
- Don't modify `uv.lock` manually — it's managed by `uv`
