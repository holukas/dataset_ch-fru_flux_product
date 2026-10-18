# Stage 10 (`10_METEO`) conventions

> Stage-specific guidance. Repo-wide conventions and the hard rules live in the
> root `CLAUDE.md`.

The stage follows the structure of the sibling CH-LAE repo, whose
`workflow/10_METEO/CLAUDE.md` holds the full conventions for the substages, the
fieldbook and its redaction, the logger programs, and the structure and checking
rules of a product notebook. Those conventions apply here unchanged; only the
site-specific facts (stations, sensors, variable names, dates) differ, and they
are recorded below as they are established.

The stage is split into three substages, numbered by decade in dependency order.
Notebook numbers restart at `01` inside each substage; a substage whose notebooks
have no dependency order carries no numbers at all.

- **`10_REFERENCE/`** — external reference data, one notebook per station,
  written to files.
- **`20_SCREENING/`** — quality screening of the site's own measurements, one
  subfolder per variable, one notebook per sensor and era. Reads the raw record
  from InfluxDB and writes the screened 30MIN series back as
  `meteoscreening_diive`.
- **`30_PRODUCTS/`** — one notebook per meteo variable, numbered in dependency
  order, each writing one product to the external data folder; a capstone `99`
  merges them.
- **`40_EXPORTS/`** — exports for other tools (e.g. the EddyPro biomet file).

The notebooks of the earlier Jupyter Book version of this repo are in
`workflow/_archive/10_METEO/`, including the meteoscreening notebooks for
2021-2025 and the diive screening template in `_TEMPLATE_/`.

## Site-specific facts (CH-FRU)

To be written.
