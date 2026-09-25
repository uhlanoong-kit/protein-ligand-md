# Reproducible workflow

## 1. Retrieve public structures

Run:

```bash
bash data/download_structures.sh
```

Retain the downloaded files unchanged in `data/raw/`.

## 2. Audit structures

Create a structure-audit table covering chain identity, mutations, missing
atoms, alternate locations, ligand identity, waters, residue numbering, and
construct comparability. Save prepared derivatives under `data/processed/`.

## 3. Parameterize

Follow [parameterization.md](parameterization.md). Record all software versions,
commands, charge decisions, warnings, and validation evidence.

## 4. Build and equilibrate

Use the version-controlled MDP files under `configs/gromacs/`. Do not advance
to production because a command finished; evaluate energy, temperature,
pressure, density, restraints, and structural geometry.

## 5. Run independent replicas

Use independent velocity seeds. Keep each replica in a separate directory.
Record hardware, GROMACS version, start structure, seed, wall time, and output
checksums where practical.

## 6. Process trajectories

Correct periodic boundaries, make molecules whole, center consistently, and
fit to the same protein atom selection. Never calculate ligand RMSD by fitting
on the ligand itself when the question concerns motion relative to the protein.

## 7. Analyze and verify

Generate RMSD, RMSF, SASA, radius of gyration, contact occupancy, hydrogen-bond
occupancy, pocket distances, and residue features. Review every replica before
combining summaries.

## 8. Interpret

Distinguish structural observations from mechanistic interpretation. Describe
sampling limitations and avoid claiming binding affinity or efficacy from
short conventional MD alone.

