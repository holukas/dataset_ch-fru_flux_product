# Dataset plan

Working document: what the CH-FRU flux product is to contain, what exists today,
and what is still missing. It is the place to look when picking up the work again.

It lives at the repository root rather than in `docs/` because Quarto renders
every `.md` under `docs/` onto the public website, and this file is internal.
When a section here settles it moves to the site — the variable inventory to
`docs/Variables.md`, the scope and coverage summary to `docs/Overview.md` — and
is deleted from this file so the two cannot drift apart.

Status vocabulary used throughout:

- **done** — exists, checked, and read by something downstream.
- **open** — planned, not started or not finished.
- **verify** — a fact this plan depends on that has not been established yet.
  Nothing marked `verify` may be quoted as settled in the published pages.


## 1. Releases

| release | period | gas analyser | state |
|---|---|---|---|
| | | | verify |


## 2. Record boundaries

| record | period | note |
|---|---|---|
| fluxes | | verify |
| meteorology | | verify |
| soil profile | | verify |


## 3. Meteorological variables

One product notebook per variable in `workflow/10_METEO/30_PRODUCTS/`, documented
on a page under `docs/Meteo_Data.md`. The list below is the set screened by the
archived 2021-2025 notebooks in `workflow/_archive/10_METEO/`.

| variable | notebook | page | state |
|---|---|---|---|
| `SW_IN` | | draft | open |
| `TA` | | draft | open |
| `PPFD_IN` | | draft | open |
| `RH` | | draft | open |
| `LW_IN` | | draft | open |
| `VPD` | | draft | open |
| `PREC` | | draft | open |
| `SWC` | | draft | open |
| `TS` | | draft | open |
| `G` | | draft | open |
| `SW_OUT` | | draft | open |
| `LW_OUT` | | draft | open |


## 4. Flux processing chain

| level | state |
|---|---|
| L0 | open |
| L1 | open |
| L2 | open |
| L3.1 | open |
| L3.2 | open |
| L3.3 | open |
| L4.1 | open |
| L4.2 | open |


## 5. Next steps

1. Port the meteo stage, following the CH-LAE `workflow/10_METEO/` structure.


## 6. Open questions

- Which gas analysers ran at CH-FRU, and over which periods? This decides whether
  the stages need per-instrument subfolders.
