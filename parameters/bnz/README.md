# BNZ parameterization

## Source

- Ligand: BNZ A200 from RCSB PDB 4W52.
- Chemical identity: benzene (`C6H6`).
- Formal and model charge: 0.
- The six deposited carbon coordinates were retained.
- Six hydrogen atoms were added reproducibly by `scripts/04_prepare_bnz.py`.

## Software and methods

- AmberTools: 23.3
- Antechamber: 22.0
- General force field: GAFF2
- GAFF2 parameter file reported by TLeap: version 2.2.20, March 2021
- Charge method: AM1-BCC
- Parameter check: `parmchk2`
- Topology validation: TLeap and ParmEd 4.3.1

## Parameterization results

- Atom count: 12
- Bond count: 12
- Atom types: six `ca` and six `ha`
- Carbon charge: -0.130000 per atom
- Hydrogen charge: +0.130000 per atom
- Total ligand charge: 0.000000
- The six deposited carbon coordinates were unchanged by Antechamber.

`parmchk2` supplied one generalized aromatic improper term:

    ca-ca-ca-ha  1.1  180.0  2.0

The term was assigned from `X-X-ca-ha` with a reported penalty score of 6.0.

## Recorded ligand validation

- TLeap reported zero errors, zero warnings, and zero notes for isolated BNZ.
- ParmEd confirmed 12 atoms, one residue, 12 bonds, 18 angles,
  and 30 dihedral entries.
- The total ligand charge was 0.000000.
- Six improper torsions were applied.
- `scripts/05_parameterize_bnz.sh` reproduced files identical to the
  committed BNZ parameters.

## Combined-system status

The dry protein-BNZ Amber topology has been validated, as documented in
[the parameterization report](../../docs/parameterization.md).

Solvation, GROMACS conversion and validation, energy minimization,
equilibration, and production simulations remain pending. Two short
contacts involving generated hydrogens in the dry complex must be
reassessed after minimization.
