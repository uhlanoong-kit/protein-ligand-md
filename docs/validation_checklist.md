# Validation checklist

## Structure

* [x] PDB/mmCIF identity and citation recorded
* [x] Chain and biological assembly justified
* [x] Mutations and construct differences compared
* [x] Missing residues, missing atoms, and alternate locations documented
* [x] Ligand identity, bond orders, formal charge, and occupancy checked
* [x] Retained or removed waters documented
* [ ] Protonation decisions recorded

## Topology

* [ ] Protein and ligand force fields are compatible
* [ ] Coordinate and topology atom counts match
* [x] Ligand charge and atom types checked
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
* Thirteen protein residues contain alternate conformations.
* Conformer A has higher occupancy for THR21, ASN53, VAL57, ASP61, ASN68, MET106, THR109, MET120, and ARG154.
* MET1, ARG14, ARG119, and ARG125 have equal A/B occupancies of 0.50.
* Residues 165–172 are unobserved in the deposited coordinates.
* The unobserved C-terminal residues are LEU165, GLU166, and HIS167–HIS172.
* Eighteen protein side-chain heavy atoms are unobserved.
* The residues affected by missing side-chain atoms are LYS16, LYS60, ARG80, ARG125, LYS147, LYS162, and ASN163.
* No internal protein backbone residue is completely missing.
* EPE A201 is one HEPES molecule containing 15 deposited atom records, each with occupancy 1.00.
* HEPES was present in the crystallization solution.
* Protein residues within 4.0 Å of EPE are GLY30, HIS31, LEU32, LYS35, ASP70, PHE104, GLN105, MET106, and GLY107.
* No EPE atom is within 5.0 Å of BNZ.
* Visual evidence is recorded in `results/figures/structure_audit/4W52_EPE_environment.png`.
* The structure contains 146 deposited HOH oxygen records, representing 146 crystallographic waters.
* No deposited crystallographic water is within 5.0 Å of BNZ.
* BNZ residue A200 is benzene with molecular formula C6H6 and molecular weight 78.112 Da.
* The complete BNZ component definition contains six carbon atoms and six hydrogen atoms.
* The deposited coordinates contain the six BNZ carbon atoms but omit the ligand hydrogen atoms.
* The BNZ carbon atoms form an aromatic ring represented by alternating single and double bonds.
* BNZ has a formal charge of 0.
* All six deposited BNZ carbon atoms have occupancy 0.70.
* The authoritative component definition is the [RCSB PDB Chemical Component Dictionary entry for BNZ](https://www.rcsb.org/ligand/BNZ).
* The last residue with deposited coordinates is LEU164.
* The entirely unobserved C-terminal extension comprises LEU165, GLU166, and HIS167–HIS172.
* The six consecutive histidines are consistent with a C-terminal affinity-tag extension.
* PDBFixer 1.12 independently detected residues 165–172 as one missing C-terminal residue block.
* PDBFixer detected exactly the 18 previously documented missing side-chain heavy atoms.
* PDBFixer detected no missing terminal atoms.
* The deposited construct is aligned to UniProt P00720 in the mmCIF reference-sequence records.
* Relative to UniProt P00720, the deposited construct contains GLY12 instead of ARG12, ALA99 instead of LEU99, and ARG137 instead of ILE137.
* The mmCIF labels GLY12/ARG12 and ARG137/ILE137 as variants and specifically labels L99A as the engineered mutation.
* Residues 165–172 are explicitly identified as the expression tag `LEHHHHHH`.
* Therefore, residues 1–164 represent the T4 lysozyme construct containing the two deposited sequence variants and the engineered L99A substitution, followed by an eight-residue C-terminal expression tag.
* A chemically complete BNZ model contains six deposited carbons and six reproducibly added hydrogens.
* The completed BNZ geometry contains six aromatic C–C bonds and six C–H bonds; its C–C distances are 1.3816–1.4001 Å and its C–H distances are 1.0900 Å.
* BNZ was parameterized using GAFF2 and AM1-BCC with AmberTools 23.3.
* GAFF2 assigned six `ca` carbon atoms and six `ha` hydrogen atoms.
* Each carbon has charge -0.130000 and each hydrogen has charge +0.130000, giving total charge 0.000000.
* `parmchk2` supplied one generalized `ca-ca-ca-ha` improper term from `X-X-ca-ha` with penalty score 6.0.
* TLeap applied six improper torsions and reported zero errors, zero warnings, and zero notes.
* ParmEd confirmed 12 atoms, one residue, 12 bonds, 18 angles, 30 dihedral entries, and total charge 0.000000.
* `scripts/05_parameterize_bnz.sh` reproduced files identical to the committed verified BNZ parameters.



### Selected decisions

* Use author chain A and biological assembly 1 because the deposited biological assembly is monomeric and chain A is the only protein chain.
* Retain conformer A for the nine alternate-location residues for which conformer A has higher occupancy.
* Preserve the original file at `data/raw/4W52.cif`; all coordinate modifications will be made in derived preparation files.
* Remove EPE A201 from the derived simulation structure. EPE is crystallization-solution HEPES, is not the target ligand, and has no atom within 5.0 Å of BNZ.
* Remove all 146 deposited crystallographic waters from the derived preparation structure. No deposited water is within 5.0 Å of BNZ. The system will subsequently be solvated using an explicit water model compatible with the selected protein force field.
* Omit the entirely unobserved C-terminal extension, residues 165–172, from the simulation structure rather than generating unsupported coordinates.
* Treat LEU164 as the final modeled protein residue; its terminal protonation state will be assigned during protein preparation.
* Use PDBFixer 1.12 to reconstruct the 18 missing side-chain heavy atoms.
* Prevent reconstruction of the unobserved C-terminal residues 165–172 by clearing PDBFixer’s missing-residue list before adding missing atoms.
* Add hydrogens only after protein and ligand protonation states have been determined.
* Parameterize neutral BNZ using GAFF2 atom types and AM1-BCC charges with AmberTools 23.3.
* Use Amber ff19SB for the protein, GAFF2 with AM1-BCC charges for BNZ, and OPC water with OPC-compatible ion parameters.
* Treat force-field compatibility as provisional until the combined topology has been generated and validated in GROMACS.

### Derived-structure verification

- `scripts/03_prepare_4W52.py` generates `data/processed/4W52_prepared_heavy_atoms.pdb` without modifying the raw mmCIF.
- The derived structure contains 1,306 protein heavy atoms and the six deposited BNZ carbon atoms.
- EPE and all crystallographic waters are absent from the derived structure.
- PDBFixer loaded and removed 128 waters without alternate locations. The remaining deposited water records comprise nine A and nine B alternate-location records that were not loaded.
- The derived protein begins at MET1 and ends at LEU164; residues 165–172 were not reconstructed.
- PDBFixer reconstructed exactly 18 missing side-chain heavy atoms.
- A second PDBFixer inspection detected zero remaining missing nonterminal heavy atoms and zero missing terminal atoms.
- All 71 deposited protein conformer-A atom records matched the derived coordinates, with no coordinate deviation above 0.002 Å.
- No hydrogens were added at this preparation stage.
- The generated PDB is an intermediate coordinate artifact and remains excluded from version control because it can be reproduced from the committed raw structure and preparation script.



### Pending decisions

* Retain conformer A for all 13 alternate-location residues. Conformer A has higher occupancy for nine residues; MET1, ARG14, ARG119, and ARG125 were visually inspected, and conformer A was selected as the deterministic tie-breaker for their equal A/B occupancies.
* Determine protein and ligand protonation states.
