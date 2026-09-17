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

