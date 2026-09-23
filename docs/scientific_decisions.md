# Scientific decision log

Record decisions chronologically. Do not silently replace a pending assumption
with a final project setting.

| Date | Decision | Evidence | Status | Consequence |
| --- | --- | --- | --- | --- |
| 2026-09-17 | Use T4 lysozyme L99A as a public benchmark | Public structures and established receptor-flexibility use | Selected | Avoids exposing private BM3 work |
| 2026-09-17 | Begin with one benzene-bound system | Keeps the first public release scientifically focused and reproducible | Selected | Compare independent replicas rather than unmatched structures |
| 2026-09-17 | Plan three independent replicas | Need to assess stochastic variation | Planned | Compute requirements must be estimated |
| 2026-09-17 | Do not report binding affinity from standard MD | Conventional short MD does not directly establish affinity | Final | Focus analysis on dynamics and interactions |
| 2026-09-18 | Retain alternate conformer A throughout 4W52 | A has higher occupancy for nine residues; four A/B ties were visually inspected, with A used as a deterministic tie-breaker | Selected | Produces one reproducible coordinate set for preparation |
| 2026-09-18 | Remove EPE A201 from the derived 4W52 simulation structure | EPE is crystallization-solution HEPES; it contacts the protein but has no atom within 5.0 Å of BNZ and is not the target ligand | Selected | Avoids parameterizing an unrelated buffer component |
| 2026-09-18 | Remove all 146 deposited crystallographic waters | No deposited water is within 5.0 Å of BNZ; the prepared system will be explicitly resolvated using a force-field-compatible water model | Selected | Provides a reproducible starting-solvent rule |
| 2026-09-18 | Treat BNZ as neutral benzene with net charge 0 | The 4W52 component definition identifies BNZ as C6H6 with an aromatic six-carbon ring; the RCSB component record reports formal charge 0 | Selected | Ligand hydrogens and force-field parameters will be generated during preparation |
| 2026-09-18 | Omit unobserved C-terminal residues 165–172 | The deposited coordinates end at LEU164; residues 165–172 are completely unobserved and include a six-histidine affinity-tag extension | Selected | LEU164 becomes the final modeled protein residue |
| 2026-09-23 | Use PDBFixer 1.12 to reconstruct the 18 missing side-chain heavy atoms | PDBFixer independently reproduced the manual audit of 18 missing side-chain heavy atoms | Selected | Clear the missing-residue list before reconstruction so residues 165–172 are not modeled; add hydrogens later |