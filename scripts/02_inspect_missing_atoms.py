#!/usr/bin/env python3
"""Inspect missing residues and atoms in 4W52 without modifying coordinates."""

from pathlib import Path

from pdbfixer import PDBFixer


INPUT_FILE = Path("data/raw/4W52.cif")

if not INPUT_FILE.is_file():
    raise FileNotFoundError(f"Input structure not found: {INPUT_FILE}")

fixer = PDBFixer(filename=str(INPUT_FILE))

fixer.findMissingResidues()

print("Missing residue blocks:")
if fixer.missingResidues:
    for (chain_index, insertion_index), residues in sorted(
        fixer.missingResidues.items()
    ):
        print(
            f"chain_index={chain_index} "
            f"insertion_index={insertion_index} "
            f"residues={','.join(residues)}"
        )
else:
    print("none")

fixer.findMissingAtoms()

print("\nMissing nonterminal heavy atoms:")
nonterminal_total = 0

for residue, atoms in fixer.missingAtoms.items():
    atom_names = [atom.name for atom in atoms]
    nonterminal_total += len(atom_names)

    print(
        f"chain={residue.chain.id} "
        f"residue={residue.name}{residue.id} "
        f"atoms={','.join(atom_names)}"
    )

print(f"Total missing nonterminal heavy atoms: {nonterminal_total}")

print("\nMissing terminal atoms:")
terminal_total = 0

for residue, atom_names in fixer.missingTerminals.items():
    terminal_total += len(atom_names)

    print(
        f"chain={residue.chain.id} "
        f"residue={residue.name}{residue.id} "
        f"atoms={','.join(atom_names)}"
    )

print(f"Total missing terminal atoms: {terminal_total}")