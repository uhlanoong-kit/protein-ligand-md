#!/usr/bin/env python3
"""Create chemically complete BNZ from deposited 4W52 carbon coordinates."""

from pathlib import Path
import shlex

import numpy as np


INPUT = Path("data/raw/4W52.cif")
OUTPUT = Path("data/processed/BNZ_complete.mol2")

CARBON_NAMES = [f"C{i}" for i in range(1, 7)]
HYDROGEN_NAMES = [f"H{i}" for i in range(1, 7)]
CH_BOND_LENGTH = 1.09  # Angstrom


def read_bnz_carbons(path):
    coordinates = {}

    for line in path.read_text().splitlines():
        if not line.startswith("HETATM "):
            continue

        fields = shlex.split(line)

        residue_name = fields[5]
        author_residue = fields[16]
        author_chain = fields[18]
        atom_name = fields[3]

        if (
            residue_name == "BNZ"
            and author_chain == "A"
            and author_residue == "200"
            and atom_name in CARBON_NAMES
        ):
            coordinates[atom_name] = np.array(
                [float(value) for value in fields[10:13]]
            )

    return coordinates


carbons = read_bnz_carbons(INPUT)

if set(carbons) != set(CARBON_NAMES):
    raise RuntimeError(
        f"Expected {CARBON_NAMES}, found {sorted(carbons)}"
    )

centroid = np.mean(
    [carbons[name] for name in CARBON_NAMES],
    axis=0,
)

hydrogens = {}

for carbon_name, hydrogen_name in zip(
    CARBON_NAMES,
    HYDROGEN_NAMES,
):
    direction = carbons[carbon_name] - centroid
    direction /= np.linalg.norm(direction)

    hydrogens[hydrogen_name] = (
        carbons[carbon_name] + CH_BOND_LENGTH * direction
    )

atoms = []

for name in CARBON_NAMES:
    atoms.append((name, carbons[name], "C.ar"))

for name in HYDROGEN_NAMES:
    atoms.append((name, hydrogens[name], "H"))

bonds = [
    ("C1", "C2", "ar"),
    ("C2", "C3", "ar"),
    ("C3", "C4", "ar"),
    ("C4", "C5", "ar"),
    ("C5", "C6", "ar"),
    ("C6", "C1", "ar"),
    ("C1", "H1", "1"),
    ("C2", "H2", "1"),
    ("C3", "H3", "1"),
    ("C4", "H4", "1"),
    ("C5", "H5", "1"),
    ("C6", "H6", "1"),
]

atom_indices = {
    name: index
    for index, (name, _, _) in enumerate(atoms, start=1)
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w") as handle:
    handle.write("@<TRIPOS>MOLECULE\n")
    handle.write("BNZ\n")
    handle.write("12 12 1 0 0\n")
    handle.write("SMALL\n")
    handle.write("USER_CHARGES\n\n")

    handle.write("@<TRIPOS>ATOM\n")

    for index, (name, coordinate, atom_type) in enumerate(
        atoms,
        start=1,
    ):
        x, y, z = coordinate
        handle.write(
            f"{index:7d} {name:<4s} "
            f"{x:10.4f} {y:10.4f} {z:10.4f} "
            f"{atom_type:<6s} 1 BNZ 0.000000\n"
        )

    handle.write("@<TRIPOS>BOND\n")

    for index, (atom1, atom2, bond_type) in enumerate(
        bonds,
        start=1,
    ):
        handle.write(
            f"{index:6d} "
            f"{atom_indices[atom1]:4d} "
            f"{atom_indices[atom2]:4d} "
            f"{bond_type}\n"
        )

    handle.write("@<TRIPOS>SUBSTRUCTURE\n")
    handle.write("1 BNZ 1 GROUP 0 **** **** 0 ROOT\n")

print(f"Input: {INPUT}")
print(f"Output: {OUTPUT}")
print("Formula: C6H6")
print("Atoms: 12")
print("Bonds: 12")
print("Formal charge: 0")
print("Aromatic ring bonds: 6")
print("Added hydrogens: 6")
print("Initial MOL2 charges are placeholders: yes")