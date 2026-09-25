# Protein-Ligand Molecular Dynamics

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GROMACS](https://img.shields.io/badge/GROMACS-target%202026.2-5B5BFF)](https://www.gromacs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-dry%20topology%20validated-orange)](#project-status)

A reproducible case study of protein-ligand molecular dynamics, designed to
demonstrate scientific study design, GROMACS simulation practice, Python data
analysis, validation, and transparent interpretation.

The public benchmark uses the benzene-bound T4 lysozyme L99A structure
(PDB 4W52). Three independent replicas are planned to assess whether ligand
and pocket behavior is reproducible across simulations. Production simulations
have not yet been run in this benchmark.

## Scientific question

Which pocket residues form persistent contacts with benzene, and how consistent
are ligand position, pocket flexibility, hydration, and solvent exposure across
independent MD replicas?

## Why this project exists

This repository is not presented as a binding-affinity predictor. It is a
small, inspectable benchmark that emphasizes:

- chemically defensible input preparation;
- separation of reference facts, project observations, and pending decisions;
- reproducible simulation and analysis settings;
- validation before interpretation;
- uncertainty across independent replicas;
- reusable residue-level feature generation.

## Workflow

1. Retrieve and audit the public structure and ligand.
2. Prepare coordinates, assign protonation states, and parameterize the system.
3. Build and validate the dry Amber complex topology.
4. Solvate, add ions, convert to GROMACS, and validate the converted system.
5. Run and validate energy minimization, NVT, and NPT equilibration in sequence.
6. Run independent production replicas with recorded velocity seeds.
7. Correct periodic-boundary artifacts and apply documented alignment selections.
8. Analyze each replica, assess uncertainty, and publish verified results.

## Project status

**Current stage: dry Amber complex topology validated; solvated GROMACS system pending.**

The status below reflects the preparation and validation recorded in the
repository. Dry-topology validation does not establish that the converted,
solvated system is ready for production MD.

| Stage | Status | Evidence or remaining work |
| --- | --- | --- |
| Study design | Documented | Benchmark question, planned replicas, and limitations recorded |
| Structure audit | Complete | Chain, alternate conformations, missing atoms, BNZ, buffer, and waters assessed |
| Heavy-atom preparation | Complete | 18 missing side-chain atoms reconstructed; derived structure checked |
| Protonation assignment | Selected and documented | Target pH 7.5; HIS31 assigned HID with uncertainty recorded |
| BNZ parameterization | Complete | Neutral GAFF2/AM1-BCC parameters generated and checked |
| Dry Amber complex topology | Validated | Atom counts, charge, ligand, HID31, parameters, and warnings reviewed |
| Solvation and GROMACS conversion | Pending | Solvated topology, ion composition, conversion, and engine-specific checks required |
| Minimization and equilibration | Not started | Geometry, energy, restraints, temperature, pressure, and density checks required |
| Production replicas | Not started | Replica settings and independent velocity seeds to be recorded |
| Trajectory analysis | Scaffold implemented | Utilities and unit tests exist; real-output integration remains pending |
| Interpretation | Not started | Requires validated trajectory results and replica-aware uncertainty |

The documented dry complex contains **2,646 atoms**, **165 residues**
(164 protein residues and one BNZ residue), and a total charge of **+8**.
Two short contacts involving generated hydrogens remain to be reassessed after
energy minimization; they are not considered resolved geometry.

Preparation decisions and validation details are recorded in:

- [Scientific decision log](docs/scientific_decisions.md)
- [Parameterization and dry-topology validation](docs/parameterization.md)
- [Validation checklist](docs/validation_checklist.md)

## Selected model and software

| Component | Recorded selection |
| --- | --- |
| Starting structure | PDB 4W52, author chain A; modeled protein residues 1â€“164 |
| Ligand | Neutral benzene, residue name BNZ |
| Protein force field | Amber ff19SB |
| Ligand parameters | GAFF2 with AM1-BCC charges |
| Planned solvent and ions | OPC water with OPC-compatible Li/Merz ion parameters |
| Target pH | 7.5; fixed protonation assignments documented separately |
| Structure preparation | PDBFixer 1.12 and OpenMM 8.6.1 |
| Parameterization | AmberTools 23.3 |
| Protonation assessment | PROPKA 3.5.1 |
| Target simulation engine | GROMACS 2026.2; converted-system validation pending |

## Next milestone

Build and validate the solvated system before starting equilibration:

1. Record the box geometry, solvent padding, and intended salt concentration.
2. Solvate with OPC water and add compatible counterions and any selected salt.
3. Convert the Amber system to GROMACS and check atom mapping, charge,
   parameters, water representation, and position restraints.
4. Record the commands, software versions, warnings, and validation outputs.
5. Run energy minimization and inspect convergence and geometry, including the
   documented short hydrogen contacts, before advancing to NVT and NPT.

## Planned analyses

- backbone RMSD and per-residue CÎ± RMSF;
- ligand RMSD after fitting on the protein;
- protein radius of gyration and SASA;
- pocket-residue distances and ligand contact occupancy;
- hydrogen-bond occupancy;
- residue-level feature table;
- agreement and uncertainty across independent replicas.

## Repository layout

| Directory | Purpose |
| --- | --- |
| `configs/` | Amber, GROMACS, and analysis settings |
| `data/` | Download instructions, system metadata, and local coordinate files |
| `docs/` | Study design, decisions, validation, and limitations |
| `parameters/` | Committed ligand parameters and provenance |
| `results/` | Audit evidence and validated analysis outputs |
| `scripts/` | Preparation and analysis commands |
| `src/` | Python analysis package |
| `tests/` | Unit tests for parsers, contact summaries, and feature construction |

## Quick start

```bash
conda env create -f environment.yml
conda activate protein-ligand-md
make download
make test
```

The download step retrieves public coordinate files only. It does not create a
validated simulation topology. Complete the structure and parameterization
checks before running MD.

Amber parameterization uses a separate environment:

```bash
conda env create -f environment-ambertools.yml
conda activate ambertools-param
```

GROMACS must be installed separately for simulation and GROMACS analysis
commands. See [the workflow](docs/workflow.md) and
[parameterization documentation](docs/parameterization.md) for the preparation
sequence and validation requirements.

### Analysis implementation status

The analysis commands are a scaffold, not a validated end-to-end workflow.
The feature-table utility currently requires two-column RMSF and SASA inputs;
it does not yet accept the mean-and-standard-deviation format produced by
per-residue SASA analysis. This integration must be corrected and tested before
using those outputs directly. Real-trajectory validation and consistent use of
the analysis configuration also remain pending.

## Evidence policy

Each scientific statement should be labeled internally as one of:

- **Reference:** reported by a cited structure, paper, or manual;
- **Observed:** measured from files produced in this project;
- **Pending:** requires calculation, literature support, or expert confirmation.

Files in `results/` are not considered evidence until the corresponding
validation checks are recorded.

## Reproducibility principles

- Raw public inputs are downloaded by script rather than silently modified.
- Derived structures receive new filenames.
- Configuration files are version controlled.
- Large trajectories and binary restart files are excluded from Git.
- Commands, software versions, warnings, and decisions are recorded.
- Replicas are analyzed separately before any combined summary is reported.

## Limitations

Short MD trajectories cannot establish binding affinity, biological efficacy,
or complete conformational convergence. Endpoint energy methods, PCA, and
clustering may be added later, but only with explicit assumptions and
validation. See [docs/limitations.md](docs/limitations.md).

## Citation and data sources

- Benzene-bound T4 lysozyme L99A: [RCSB PDB 4W52](https://www.rcsb.org/structure/4W52)
- Project citation metadata: [CITATION.cff](CITATION.cff)

## License

The original code and documentation in this repository are released under the
[MIT License](LICENSE). Downloaded structures and third-party tools remain
subject to their respective terms and citation requirements.