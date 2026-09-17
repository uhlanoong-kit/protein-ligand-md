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
