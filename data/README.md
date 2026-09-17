# Data provenance

This directory contains scripts and metadata, not committed raw trajectories.

## Public structures

| Role | PDB ID | Intended use | Status |
| --- | --- | --- | --- |
| Benzene-bound system | 4W52 | Primary protein-ligand benchmark | Reference selected |

Run `bash data/download_structures.sh` to download mmCIF coordinate files from
RCSB PDB into `data/raw/`.

Before simulation, record:

- construct and mutation agreement;
- chain selection;
- missing residues and atoms;
- alternate conformations;
- ligand identity and occupancy;
- crystallographic waters retained or removed;
- protonation and tautomer decisions;
- biological assembly decision.

Do not commit private laboratory inputs, licensed software, raw trajectories,
or unpublished parameter files.
