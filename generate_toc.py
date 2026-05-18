"""Generate myst.yml (JupyterBook 2) from the notebooks folder structure.

Run whenever notebooks are added or moved:
    uv run python generate_toc.py
"""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent
NB_ROOT = ROOT / "notebooks"

EXCLUDE_DIRS = {".ipynb_checkpoints", "_TEMPLATE_"}
EXCLUDE_PREFIXES = ("x-", "x_", "xC")  # skip deprecated/scratch notebooks


def iter_notebooks(folder: Path) -> list[Path]:
    nbs = []
    for p in sorted(folder.iterdir()):
        if p.is_file() and p.suffix == ".ipynb":
            if not p.name.startswith(EXCLUDE_PREFIXES):
                nbs.append(p)
    return nbs


def rel(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


# --- Root document (landing page) ---
# Use docs/intro.md if it exists, otherwise create a minimal stub.
intro = ROOT / "docs" / "intro.md"
if not intro.exists():
    intro.write_text("# CH-FRU Flux Dataset Preparation\n\nWelcome.\n", encoding="utf-8")
    print(f"Created stub: {intro}")

# --- All other .md files in docs/ become top-level TOC entries ---
other_docs = [
    {"file": rel(p)}
    for p in sorted((ROOT / "docs").glob("*.md"))
    if p != intro
]

# --- Meteoscreening chapter ---
meteo_children = []
meteo_root = NB_ROOT / "10_METEO"

for nb in iter_notebooks(meteo_root):
    meteo_children.append({"file": rel(nb)})

screening_root = meteo_root / "11_meteoscreening_diive_2021-2025"
if screening_root.exists():
    for var_dir in sorted(screening_root.iterdir()):
        if var_dir.is_dir() and var_dir.name not in EXCLUDE_DIRS:
            nbs = iter_notebooks(var_dir)
            if nbs:
                meteo_children.append({
                    "title": var_dir.name,
                    "children": [{"file": rel(nb)} for nb in nbs],
                })

# --- Full TOC ---
toc = other_docs + [
    {"title": "Meteoscreening", "children": meteo_children},
    {"file": "notebooks/02_outlier_detection"},
    {"file": "notebooks/03_gapfilling"},
    {"file": "notebooks/04_final_dataset"},
]

# --- Assemble full myst.yml ---
myst = {
    "version": 1,
    "project": {
        "title": "CH-FRU Flux Dataset Preparation",
        "authors": [{"name": "Lukas Hörtnagl", "email": "lukas.hoertnagl@usys.ethz.ch"}],
        "github": "https://github.com/holukas/dataset-ch-fru-flux-product",
        "index": rel(intro),
        "toc": toc,
    },
    "site": {
        "template": "book-theme",
        "options": {
            "base_url": "/dataset_ch-fru_flux_product",
            "stylesheet": "_static/custom.css",
        },
    },
}

out = ROOT / "myst.yml"
out.write_text(yaml.dump(myst, allow_unicode=True, sort_keys=False, default_flow_style=False), encoding="utf-8")
print(f"Written {out}")
print(f"Root: {rel(intro)}")
print(f"TOC entries: {len(toc)}")
