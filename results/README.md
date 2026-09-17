# Results policy

Commit only compact, verified results that can be regenerated from documented
inputs and scripts.

- `figures/`: publication-quality PNG or SVG figures.
- `tables/`: compact CSV summaries and residue-level features.
- `raw/`: generated local analysis outputs; ignored by Git.

Do not add fabricated placeholder results. Every committed figure should have a
caption in the final report describing the system, replicas, time range,
selection, units, and uncertainty.

