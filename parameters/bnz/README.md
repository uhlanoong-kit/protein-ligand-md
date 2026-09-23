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

```text
ca-ca-ca-ha  1.1  180.0  2.0
validation remain pending.