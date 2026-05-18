# CH-FRU Flux Dataset — Project Guide

## What this project is

A Jupyter Book documenting the preparation of the CH-FRU eddy covariance grassland flux dataset:
meteoscreening → outlier detection → gap-filling → final dataset.

The book is published as a static HTML site on GitHub Pages.

## Environment

- Python 3.12, managed with **uv**
- Install: `uv sync --dev`
- Local packages (editable): `diive` (`../../21 - DIIVE/diive`) and `dbc-influxdb` (`../../22 - POET/dbc-influxdb`)

## Key commands

```powershell
# After adding/moving notebooks, regenerate myst.yml TOC
uv run python generate_toc.py

# Preview locally (live dev server, opens browser)
uv run jupyter-book start

# Clean build artifacts (requires -y to skip confirmation)
uv run jupyter-book clean -y

# Build static HTML for deployment (BASE_URL needed for GitHub Pages subpath)
# On Windows (Git Bash / uv run):
MSYS_NO_PATHCONV=1 BASE_URL="/dataset_ch-fru_flux_product" uv run jupyter-book build --html

# Deploy to GitHub Pages (after build --html)
uv run ghp-import -n -p -f _build/html
```

Note: `jupyter-book build` (without `--html`) builds JSON content only.
`--html` produces the full static site in `_build/html/` needed for `ghp-import`.

## Project structure

```
myst.yml             # Jupyter Book 2 config + table of contents — DO NOT edit by hand, use generate_toc.py
_config.yml          # Legacy JB1 config (kept for reference, not used by JB2)
_toc.yml             # Legacy JB1 TOC (kept for reference, not used by JB2)
generate_toc.py      # Script that auto-generates myst.yml from the notebooks/ folder
docs/                # Markdown narrative pages — edit these in Obsidian
notebooks/           # Jupyter notebooks (pre-built, outputs committed)
  10_METEO/          # Meteoscreening notebooks
    11_meteoscreening_diive_2021-2025/
      G/ LW/ PPFD/ PREC/ RH/ SW/ SWC/ TA/ TS/   # per-variable, grouped by type
    12.x_  13.x_  16.x_  A1_  A3_                # download, merge, gap-filling
data/                # gitignored — raw and intermediate data files
```

## Notebooks — important rules

- **Pre-built**: `execute_notebooks: "off"` in `_config.yml`. Run notebooks locally in Jupyter, save with outputs, commit the `.ipynb`.
- **Never commit checkpoint files**: `.ipynb_checkpoints/` is gitignored.
- **Data files** (`.csv`, `.parquet`, `.zip`) live in `data/` or stay gitignored — do not commit them inside `notebooks/`.
- **Excluded from TOC**: `_TEMPLATE_/` folder and files with `x-` prefix (deprecated/scratch).

## Writing prose

- Point an Obsidian vault at the `docs/` folder.
- Files are plain Markdown (CommonMark). MyST directives like ` ```{note} ` show as code fences in Obsidian but render correctly in the book.

## Adding new notebooks

1. Place the notebook in the appropriate `notebooks/` subfolder.
2. Run `uv run python generate_toc.py` to update `_toc.yml`.
3. Build and verify: `uv run jupyter-book build .`

## GitHub Pages

- Repo: `https://github.com/holukas/dataset-ch-fru-flux-product`
- Pages branch: `gh-pages` (managed by `ghp-import`)
- Enable in repo Settings → Pages → Source: `gh-pages` branch

## Dependencies

| Package | Purpose |
|---|---|
| `jupyter-book>=2.1.5` | Book builder (Sphinx-based) |
| `ghp-import>=2.1.0` | Deploy `_build/html` to `gh-pages` branch |
| `sphinxcontrib-mermaid` | Mermaid diagram support in book |
| `diive` | Flux data processing (local editable) |
| `dbc-influxdb` | InfluxDB data access (local editable) |
