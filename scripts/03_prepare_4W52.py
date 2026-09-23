#!/usr/bin/env python3
"""Prepare a heavy-atom 4W52 structure without modifying the raw mmCIF."""

from pathlib import Path

from openmm.app import Modeller, PDBFile
from pdbfixer import PDBFixer


INPUT = Path("data/raw/4W52.cif")
OUTPUT = Path("data/processed/4W52_prepared_heavy_atoms.pdb")

EXPECTED_MISSING_ATOMS = {
    ("A", "16", "LYS"): {"NZ"},
    ("A", "60", "LYS"): {"NZ"},
    ("A", "80", "ARG"): {"CG", "CD", "NE", "CZ", "NH1", "NH2"},
    ("A", "125", "ARG"): {"CZ", "NH1", "NH2"},
    ("A", "147", "LYS"): {"NZ"},
    ("A", "162", "LYS"): {"CD", "CE", "NZ"},
    ("A", "163", "ASN"): {"CG", "OD1", "ND2"},
}


def detected_missing_atoms(fixer):
    result = {}

    for residue, atoms in fixer.missingAtoms.items():
        key = (residue.chain.id, residue.id, residue.name)
        result[key] = {atom.name for atom in atoms}

    return result


if not INPUT.is_file():
    raise FileNotFoundError(f"Input structure not found: {INPUT}")

fixer = PDBFixer(filename=str(INPUT))

# Detect but deliberately do not reconstruct residues 165–172.
fixer.findMissingResidues()
detected_missing_residues = dict(fixer.missingResidues)

expected_missing_residues = {
    (0, 164): ["LEU", "GLU", "HIS", "HIS", "HIS", "HIS", "HIS", "HIS"]
}

if detected_missing_residues != expected_missing_residues:
    raise RuntimeError(
        "Unexpected missing-residue result: "
        f"{detected_missing_residues}"
    )

fixer.missingResidues = {}

# Detect and validate the missing side-chain heavy atoms.
fixer.findMissingAtoms()
detected = detected_missing_atoms(fixer)

if detected != EXPECTED_MISSING_ATOMS:
    raise RuntimeError(f"Unexpected missing-atom result: {detected}")

missing_atom_count = sum(len(atoms) for atoms in detected.values())

if missing_atom_count != 18:
    raise RuntimeError(
        f"Expected 18 missing heavy atoms, detected {missing_atom_count}"
    )

fixer.addMissingAtoms()

# Remove crystallographic waters and EPE while retaining BNZ.
modeller = Modeller(fixer.topology, fixer.positions)
residues_to_remove = [
    residue
    for residue in modeller.topology.residues()
    if residue.name in {"HOH", "EPE"}
]
modeller.delete(residues_to_remove)

remaining_residues = list(modeller.topology.residues())

if any(residue.name in {"HOH", "EPE"} for residue in remaining_residues):
    raise RuntimeError("EPE or crystallographic water remains after removal")

bnz_residues = [
    residue for residue in remaining_residues if residue.name == "BNZ"
]

if len(bnz_residues) != 1:
    raise RuntimeError(
        f"Expected one BNZ residue, found {len(bnz_residues)}"
    )

bnz_atom_count = sum(1 for _ in bnz_residues[0].atoms())

if bnz_atom_count != 6:
    raise RuntimeError(
        f"Expected six deposited BNZ atoms, found {bnz_atom_count}"
    )

# Confirm that no omitted C-terminal residues were reconstructed.
protein_residues = [
    residue for residue in remaining_residues if residue.name != "BNZ"
]
last_residue = protein_residues[-1]

if last_residue.name != "LEU" or last_residue.id != "164":
    raise RuntimeError(
        f"Unexpected final protein residue: "
        f"{last_residue.name}{last_residue.id}"
    )

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w") as handle:
    PDBFile.writeFile(
        modeller.topology,
        modeller.positions,
        handle,
        keepIds=True,
    )

print(f"Input: {INPUT}")
print(f"Output: {OUTPUT}")
print(f"Reconstructed heavy atoms: {missing_atom_count}")
# print(f"Removed residues: {len(residues_to_remove)}")

removed_waters = sum(
    residue.name == "HOH" for residue in residues_to_remove
)
removed_epe = sum(
    residue.name == "EPE" for residue in residues_to_remove
)

print(
    f"Removed loaded residues: {len(residues_to_remove)} "
    f"({removed_waters} HOH and {removed_epe} EPE)"
)
print(f"Remaining BNZ atoms: {bnz_atom_count}")
print(f"Final protein residue: {last_residue.name}{last_residue.id}")
print("Hydrogens added: 0")