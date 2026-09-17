# Study design

## Objective

Evaluate benzene and local pocket behavior in the T4 lysozyme L99A benchmark
while demonstrating a transparent and reproducible MD workflow.

## Primary question

Which pocket residues form persistent contacts with benzene, and how consistent
are ligand position, pocket flexibility, hydration, and SASA across independent
replicas?

## Systems

- **Protein-ligand benchmark:** PDB 4W52.
- **Ligand:** benzene, residue name BNZ in the deposited structure.

## Planned design

1. Audit and prepare the structure using documented rules.
2. Parameterize protein and ligand with a compatible, cited force-field stack.
3. Minimize and equilibrate the system using a validated protocol.
4. Run at least three independent replicas when compute resources permit.
5. Analyze replicas independently using identical selections and time windows.
6. Report distributions and uncertainty rather than a single mean trajectory.

## Evidence classes

- **Reference:** sourced from PDB, literature, or software documentation.
- **Observed:** measured from generated and validated project files.
- **Pending:** awaiting calculation or a documented scientific decision.

## Success criteria

- reproducible preparation log;
- no unresolved topology errors;
- stable thermodynamic equilibration evidence;
- valid periodic-boundary treatment and alignment;
- separate replica summaries;
- conclusions proportional to sampling and uncertainty.
