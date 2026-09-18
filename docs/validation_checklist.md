# Validation checklist

## Structure

- [ ] PDB/mmCIF identity and citation recorded
- [ ] chain and biological assembly justified
- [ ] mutations and construct differences compared
- [ ] missing residues, atoms, and alternate locations documented
- [ ] ligand identity, bond orders, formal charge, and occupancy checked
- [ ] retained or removed waters documented
- [ ] protonation decisions recorded

## Topology

- [ ] protein and ligand force fields are compatible
- [ ] coordinate and topology atom counts match
- [ ] ligand charge and atom types checked
- [ ] no unexplained missing parameters
- [ ] topology warnings reviewed individually

## Simulation

- [ ] minimization converged to the stated criterion
- [ ] temperature is stable around the target
- [ ] pressure and density are evaluated over an appropriate window
- [ ] restraints behave as intended
- [ ] no unstable bond, volume, or energy behavior
- [ ] independent seeds recorded for each replica

## Trajectory processing

- [ ] periodic-boundary artifacts removed
- [ ] molecules are whole
- [ ] centering and fit selections recorded
- [ ] processed frame count and time range verified

## Analysis

- [ ] each replica inspected separately
- [ ] analysis selections are identical across systems
- [ ] units and time windows are explicit
- [ ] uncertainty is reported
- [ ] figures can be regenerated from committed code
- [ ] interpretation does not exceed the available sampling

## 4W52 manual audit notes

### Observed

- Structure contains one protein author chain, chain A.
- Biological assembly is monomeric.
- Deposited construct contains the L99A mutation.
- Ligand BNZ contains six atoms at residue 200.
- Deposited BNZ occupancy is 0.70.
- Structure contains 15 EPE atoms.
- Structure contains 146 crystallographic water atoms.
- Thirteen protein residues contain alternate conformations.
- Residues 165–172 are unobserved in the coordinates.

### Pending decisions

- Select one conformation for each alternate-location residue.
- Determine whether EPE should be removed.
- Determine which crystallographic waters should be retained.
- Omit or model the unobserved C-terminal residues.

