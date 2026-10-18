# Stage 00 (`00_L0_checks`) and the EC setup

> Stage-specific guidance. Repo-wide conventions and the hard rules live in the
> root `CLAUDE.md`.

Level 0 is the preliminary flux calculation. EddyPro is run **per setup period**,
so this stage merges the per-run *FLUXNET* output files into one 30MIN record per
gas analyser and then checks that record — fluxes, wind direction, time lags —
before anything downstream reads it. The merge notebook computes and corrects
nothing beyond dropping columns that do not belong; the check notebooks export
nothing.

The general lessons recorded for this stage in the sibling CH-LAE repo
(`workflow/00_L0_checks/CLAUDE.md` there) apply here too: merge on the timestamps
inside the files, never on the file names; judge a gas-analyser fault on a gas
flux, not on `H`; time lags are not comparable across setup periods. The
site-specific facts of the CH-FRU setup are still to be written.
