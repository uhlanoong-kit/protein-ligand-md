# Validation checklist

## Structure

* [x] PDB/mmCIF identity and citation recorded
* [x] Chain and biological assembly justified
* [ ] Mutations and construct differences compared
* [x] Missing residues, missing atoms, and alternate locations documented
* [ ] Ligand identity, bond orders, formal charge, and occupancy checked
* [ ] Retained or removed waters documented
* [ ] Protonation decisions recorded

## Topology

* [ ] Protein and ligand force fields are compatible
* [ ] Coordinate and topology atom counts match
* [ ] Ligand charge and atom types checked
* [ ] No unexplained missing parameters
* [ ] Topology warnings reviewed individually

## Simulation

* [ ] Minimization converged to the stated criterion
* [ ] Temperature is stable around the target
* [ ] Pressure and density are evaluated over an appropriate window
* [ ] Restraints behave as intended
* [ ] No unstable bond, volume, or energy behavior
* [ ] Independent seeds recorded for each replica

## Trajectory processing

* [ ] Periodic-boundary artifacts removed
* [ ] Molecules are whole
* [ ] Centering and fitting selections recorded
* [ ] Processed frame count and time range verified

## Analysis

* [ ] Each replica inspected separately
* [ ] Analysis selections are identical across systems
* [ ] Units and time windows are explicit
* [ ] Uncertainty is reported
* [ ] Figures can be regenerated from committed code
* [ ] Interpretation does not exceed the available sampling

## 4W52 manual audit notes

### Reference

* Structure: RCSB PDB 4W52, “T4 Lysozyme L99A with Benzene Bound.”
* Experimental method: X-ray diffraction.
* Resolution: 1.50 Å.
* PDB DOI: https://doi.org/10.2210/pdb4w52/pdb
* Primary publication: Merski et al. (2015), “Homologous ligands accommodated by discrete conformations of a buried cavity.”
* Publication DOI: https://doi.org/10.1073/pnas.1500806112

### Observations

* The structure contains one protein author chain, chain A.
* The deposited biological assembly is monomeric.
* The deposited construct contains the L99A mutation.
* BNZ residue 200 contains six deposited carbon-atom records; ligand hydrogen atoms are not present.
* The deposited occupancy of every BNZ atom is 0.70.
* The structure contains 15 deposited EPE atom records.
* The structure contains 146 deposited HOH oxygen records, representing 146 crystallographic waters.
* Thirteen protein residues contain alternate conformations.
* Residues 165–172 are unobserved in the deposited coordinates.
* The unobserved C-terminal residues are LEU165, GLU166, and HIS167–HIS172.
* Eighteen protein side-chain heavy atoms are unobserved.
* The residues affected by missing side-chain atoms are LYS16, LYS60, ARG80, ARG125, LYS147, LYS162, and ASN163.
* No internal protein backbone residue is completely missing.
* Conformer A has higher occupancy for THR21, ASN53, VAL57, ASP61, ASN68, MET106, THR109, MET120, and ARG154.
* MET1, ARG14, ARG119, and ARG125 have equal A/B occupancies of 0.50.

### Selected decisions

* Use author chain A and biological assembly 1 because the deposited biological assembly is monomeric and chain A is the only protein chain.
* Retain conformer A for the nine alternate-location residues for which conformer A has higher occupancy.
* Preserve the original file at `data/raw/4W52.cif`; all coordinate modifications will be made in derived preparation files.

### Pending decisions

* Visually inspect MET1, ARG14, ARG119, and ARG125 before applying an A/B tie-breaking rule.
* Determine whether EPE will be removed during preparation.
* Determine which crystallographic waters, if any, will be retained.
* Decide whether to omit or model the unobserved C-terminal residues 165–172.
* Select and document a reproducible method for reconstructing the 18 missing side-chain heavy atoms.
* Verify the BNZ chemical structure, bond orders, formal charge, and parameterization method.
* Determine protein and ligand protonation states.
