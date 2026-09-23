# Parameterization plan

Parameterization is a scientific decision, not a file-conversion step.

## Protein

Select a current protein force field and compatible water model. Record the
exact versions and any modifications.

## Ligand

For benzene, record:

- source structure and residue name;
- bond orders and aromaticity;
- hydrogen addition;
- formal and model charge;
- atom-typing and charge method;
- force-field version;
- warnings, missing parameters, and penalty scores;
- conversion method if parameters originate outside GROMACS.

## Required validation

- ligand total charge is correct;
- atom names map consistently between coordinates and topology;
- no missing bonded or nonbonded parameters remain;
- topology is readable by the selected GROMACS version;
- minimized ligand geometry remains chemically plausible;
- minimized protein-ligand geometry remains chemically plausible.

No ligand topology is committed in the design-stage release because it has not
yet been generated and independently verified.

## Selected BNZ method

BNZ is parameterized as neutral benzene using GAFF2 atom types and AM1-BCC
charges with AmberTools 23.3. The deposited six-carbon coordinates are retained,
and six hydrogens are added by `scripts/04_prepare_bnz.py`.

The complete parameterization and validation workflow is implemented by
`scripts/05_parameterize_bnz.sh`. Verified files and detailed provenance are
stored under `parameters/bnz/`.

## Selected force-field stack

- Protein: Amber ff19SB from AmberTools 23.3.
- Ligand: GAFF2 with AM1-BCC charges generated using AmberTools 23.3.
- Water: OPC.
- Ions: OPC-compatible Li/Merz parameters loaded by `leaprc.water.opc`.
- Target simulation engine: GROMACS 2026.2.

The local AmberTools installation loads `frcmod.ff19SB`,
`amino19.lib`, `aminoct12.lib`, and `aminont12.lib` for ff19SB.
For OPC, it loads `frcmod.opc` and `frcmod.ionslm_126_opc`.

Compatibility remains provisional until a combined protein–BNZ topology is
generated, converted to GROMACS format, and checked for missing parameters,
atom-count consistency, and conversion warnings.

## Selected protonation states

Protonation states were assessed for a target pH of 7.5, matching the
deposited crystallization pH. PROPKA 3.5.1 was run on the prepared heavy-atom
structure.

- ASP and GLU residues are deprotonated.
- LYS and ARG residues are protonated.
- TYR residues remain neutral.
- CYS54 and CYS97 remain neutral thiols. Their sulfur atoms are 29.181 Å
  apart, excluding a disulfide bond.
- MET1 uses a positively charged N-terminus.
- LEU164 uses a negatively charged C-terminus.
- BNZ remains neutral.
- HIS31 is assigned the neutral Amber `HID` state, with its proton on ND1.

PROPKA predicted a pKa of 7.34 for HIS31. At pH 7.5, the neutral form is the
majority state, although the predicted value indicates meaningful uncertainty.
The 2.728 Å HIS31 ND1–ASP70 OD2 distance supports an ND1-H hydrogen bond and
therefore the `HID` tautomer.

PROPKA reported a terminal-group warning for LEU164, but manual inspection
confirmed that both O and OXT are present. Their C–O distances are 1.233 and
1.267 Å, respectively. The warning was therefore reviewed and does not indicate
a missing terminal oxygen.
