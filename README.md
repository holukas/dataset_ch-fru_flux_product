# dataset_ch-fru_flux_product

Methods documentation and processing notebooks for the **CH-FRU flux product**,
the PI dataset of the grassland station
[CH-FRU (Früebüel)](https://www.swissfluxnet.ethz.ch/index.php/sites/site-info-ch-fru/).
The site is part of [Swiss FluxNet](https://www.swissfluxnet.ethz.ch/), operated
by the [Grassland Sciences Group, ETH Zurich](https://gl.ethz.ch/).

**Published site: <https://holukas.github.io/dataset_ch-fru_flux_product/>**

**Author**: [Lukas Hörtnagl](https://gl.ethz.ch/people/person-detail.lukas.html)

> **The dataset is in preparation.** Both the data and this documentation are
> work in progress and subject to change. Please contact the author before using
> the data.

## Scope

The dataset comprises ecosystem fluxes measured by the eddy covariance method
(CO<sub>2</sub>, H<sub>2</sub>O, H), meteorological data and management
information.

This repository holds the **methods narrative and the notebooks that produce the
product**. The flux computation itself (EddyPro) and the meteo screening runs
happen in a separate offline pipeline; what is documented here is how their
output is checked, corrected, merged and exported.

The repository is set up in the same way as its sibling,
[`dataset_ch-lae_flux_product`](https://github.com/holukas/dataset_ch-lae_flux_product),
and the two are developed in parallel.

## Layout

| Path | Contents |
| --- | --- |
| [`docs/`](docs/) | The reader-facing [Quarto website](https://holukas.github.io/dataset_ch-fru_flux_product/). Single config file [`docs/_quarto.yml`](docs/_quarto.yml). |
| [`workflow/`](workflow/) | The working notebooks and scripts, by numbered stage. Research scratch space, rendered onto the site as a notebook appendix but not part of the curated narrative. |
| `workflow/_archive/`, `workflow/_templates/` | Reserved: dead or experimental work (mirroring the stage layout), and reusable notebook templates. Both are excluded from the site build. |

### Workflow stages

| Stage | Purpose |
| --- | --- |
| `00_L0_checks/` | Level-0 preliminary flux calculation and its checks. |
| `10_METEO/` | Meteo, in three substages — `10_REFERENCE/` (external reference series), `20_SCREENING/` (per-variable, per-sensor stepwise screening), `30_PRODUCTS/` (one product notebook per variable, joined into one merged file) — plus `40_EXPORTS/`. |
| `20_MERGE_DATA/` | Merge Level-1 fluxes with the meteo product. |
| `30_FLUX_PROCESSING_CHAIN/` | The flux processing chain from Level-2 to Level-4.2. |
| `90_DATASET_OVERVIEW/` | Dataset-wide overview notebooks and the generators for standalone HTML products. |

### Data files live outside this repository

Only code, prose and figures are tracked here. The data the notebooks read and
write is too heavy for git and lives in an untracked folder:

```
F:\Sync\luhk_work\dev-data\datasets-data\dataset_ch-fru_flux_product-data\workflow\
```

That tree is **mirrored 1:1** with `workflow/`: same stage folders, same
instrument subfolders, and a data file carries the same numeric prefix and
relative path as the notebook that produces it.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12–3.13. The environment
also vendors Quarto (as the `quarto-cli` dev dependency), so no separate Quarto
installation is needed.

```bash
uv sync
```

Note that [`diive`](https://github.com/holukas/diive) is declared as an editable
path dependency at `../../diive`, so a checkout of that repository must exist two
levels up from this one. Some notebooks additionally read the InfluxDB database
through `diive`'s `InfluxIO`.

## Building the site

Three PowerShell wrappers at the repo root drive the build; they exist so the
step order does not have to be remembered.

```bash
./preview_fast.ps1
```

Live-reload dev server for the narrative pages only — no notebooks, so
`/notebooks/` links will not resolve.

```bash
./preview_full.ps1
```

Full local build (website **and** notebooks) served over real HTTP, so search
and the notebook pages work. The check to run before deploying.

```bash
./deploy.ps1
```

The single deploy entry point: stages the notebooks, renders the site, clears
the staging, builds the dashboards (once their builders exist), and publishes
`docs/_build/html` to the `gh-pages` branch with `ghp-import`. `-Preview` builds
and serves, `-NoPublish` builds only, `-NoDashboards` skips the dashboard steps.
It touches only `gh-pages`, never the source branch or working tree.

Under the wrappers the manual sequence is, in this order:

```bash
uv run python build_notebooks.py && uv run quarto render docs && uv run python build_notebooks.py --clean
```

## Helper scripts

| Script | Purpose |
| --- | --- |
| [`build_notebooks.py`](build_notebooks.py) | Stage `workflow/**/*.ipynb` into `docs/notebooks/` for the Quarto render; `--clean` removes the staging. |
| [`build_fieldbook_md.py`](build_fieldbook_md.py) | Render the GIN fieldbook export as one readable, redacted markdown file. Writes beside the export in the external data folder, never into this repository. |
| [`check_no_names.py`](check_no_names.py) | Fail if any name from the fieldbook redaction map appears anywhere in the repository. Run before publishing. |

## Conventions

- [`CLAUDE.md`](CLAUDE.md) — repository-wide rules, layout and writing register.
- [`workflow/00_L0_checks/CLAUDE.md`](workflow/00_L0_checks/CLAUDE.md) and
  [`workflow/10_METEO/CLAUDE.md`](workflow/10_METEO/CLAUDE.md) — stage guidance.
- `.claude/rules/docs.md` — the Quarto website: build mechanics, notebook
  staging, markup conventions, and how the pages are organized. The `.claude/`
  folder is not part of this repository: it is kept in the external data folder
  and linked in locally.

Two rules are worth stating up front, because both are enforced:

- **No real person's name goes into this repository.** Quoted fieldbook strings
  are redacted, and names in prose and code comments count too.
  `check_no_names.py` scans the repository and exits non-zero. Published credit
  — acknowledgements, citations, photo credits, the author byline — is
  deliberate and exempt.
- **Filenames** carry no spaces and no `+` (use `_and_`).

## Licence

[GNU General Public License v3.0](LICENSE).
