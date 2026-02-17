# Copilot Instructions for fredmontet

This is a **Quarto website project** - a static site generator for publishing content with integrated support for code, data, and narrative.

## Project Overview

- **Type**: Personal website/portfolio built with Quarto
- **Source files**: `*.qmd` (Quarto markdown files in root and `stories/`)
- **Output**: Static HTML generated to `_site/` directory
- **Styling**: Custom SCSS theme applied via `theme.scss` + sandstone base theme
- **Configuration**: All settings in `_quarto.yml`
- **Package management**: UV (fast Python package manager)
- **Build automation**: Makefile with common targets

## Key Workflows

### Building & Previewing
- **Preview locally**: `make preview` or `uv run quarto preview`
- **Build static site**: `make build` or `uv run quarto render` (outputs to `_site/`)
- **Full dev setup**: `make dev` (syncs dependencies + starts preview server)
- **Production build**: `make publish` (cleans artifacts + builds)
- **Both**: The preview server auto-rebuilds on `.qmd` or `.scss` changes

### Environment Setup
- **Install dependencies**: `make sync` or `uv sync` (reads from `pyproject.toml`)
- **Add packages**: `uv add package-name` (updates `pyproject.toml` and `uv.lock`)
- **Dependencies**: altair, pandas, numpy, jupyter, pyyaml (see `pyproject.toml`)
- **All commands run through UV**: Use `uv run` prefix or `make` targets, not bare `quarto`

### File Organization
- **Page content**: Each `.qmd` file becomes an HTML page
  - Root level: `index.qmd`, `research.qmd`, `stories.qmd` (main pages)
  - `stories/` directory: Contains different story formats, one directory per story
- **Navigation**: Configured in `_quarto.yml` under `website.navbar`
- **Styling**: `theme.scss` with custom SCSS variables and responsive design

## Story Formats

Four distinct story types in `stories/` folder, each in its own directory:

1. **Thought** (`stories/thought-*/index.qmd`)
   - Tweet-like format, short and concise
   - Wrapped in `::: {.thought}` div
   - Category: `thought`

2. **Data Story** (`stories/data-story-*/index.qmd`)
   - Jupyter-executable with Python code blocks (`jupyter: python3` in frontmatter)
   - Interactive Altair visualizations
   - Supports methodology, analysis, and references

3. **Long-form Story** (`stories/story-*/index.qmd`)
   - Extended narrative with depth
   - Blockquotes with `>` syntax
   - Highlighted text using `==text==`
   - Structured sections and references

4. **Photographic Story** (`stories/photographic-story-*/index.qmd`)
   - Image-focused narratives with `lightbox: true` in frontmatter
   - Image groups for gallery display
   - Styled with rounded corners and shadows

Each story directory may contain a `references.bib` for citations (`[@key]` syntax).

## Development Patterns

### Quarto Markdown (.qmd)
- **YAML frontmatter** at top defines metadata (title, date, categories, jupyter kernel)
- **Content**: Standard Markdown below frontmatter
- **Jupyter execution**: Add `jupyter: python3` in frontmatter to enable code execution

### Styling SCSS Patterns
- **Fonts**: Noto Sans (body), Noto Serif (headings), Noto Sans Mono (code)
- `==highlighted text==` → yellow background highlight
- `> blockquote` → left border with italic text
- Image captions: Auto-styled with smaller font and center alignment
- Code blocks: Light gray background with monospace font
- Responsive breakpoint at 768px

### Adding New Pages
1. Create `.qmd` file with YAML frontmatter
2. Update `website.navbar.left` in `_quarto.yml`
3. Reference via `href: filename.qmd`

### Adding Story Posts
1. Create directory in `stories/` with appropriate prefix: `thought-`, `data-story-`, `story-`, `photographic-story-`
2. Add `index.qmd` with proper frontmatter (title, date, categories)
3. Add `references.bib` if citations are needed

## Important Notes

- **`_site/` is generated**: Never edit directly; rebuild with `make build`
- **`.quarto/` is cached**: Ignore this directory; stores intermediate artifacts
- **`uv.lock` tracks dependencies**: Commit this file for reproducible environments
- **Don't modify `uv.lock` manually**: It's managed by `uv`
- **Python >=3.11 required**: Due to pandas/numpy compatibility
- **Data stories need Jupyter**: Quarto executes Python code in data story templates

## Quick Reference

| Task | Command |
|------|---------|
| Install dependencies | `make sync` or `uv sync` |
| Preview site | `make preview` or `uv run quarto preview` |
| Full dev setup | `make dev` |
| Build site | `make build` or `uv run quarto render` |
| Production build | `make publish` |
| Clean artifacts | `make clean` |
| Add package | `uv add package-name` |
| New page | Create `.qmd`, update navbar in `_quarto.yml` |
| New story | Create directory in `stories/` with type prefix, add `index.qmd` |
| Customize theme | Edit `theme.scss` |
