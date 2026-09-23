#!/usr/bin/env python3
"""Prepare the protein-only Amber input for 4W52.

This script:
- retains protein ATOM records from residues 1–164;
- removes BNZ and all other HETATM records;
- renames HIS31 to the selected Amber HID tautomer;
- removes the existing LEU164 OXT so TLeap can rebuild it;
- preserves all other heavy-atom coordinates;
- does not add hydrogens.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT = PROJECT_ROOT / "data/processed/4W52_prepared_heavy_atoms.pdb"
OUTPUT = PROJECT_ROOT / "data/processed/4W52_protein_HID.pdb"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(
            f"Missing input: {INPUT}\n"
            "Run scripts/03_prepare_4W52.py first."
        )

    output_lines: list[str] = []
    atom_count = 0
    hid_atom_count = 0
    removed_terminal_oxt = 0
    changed_residues: set[tuple[str, int]] = set()
    residue_numbers: list[int] = []

    with INPUT.open() as handle:
        for line in handle:
            if not line.startswith("ATOM"):
                continue

            atom_name = line[12:16].strip()
            residue_name = line[17:20].strip()
            chain = line[21].strip()
            residue_number = int(line[22:26])

            if chain != "A":
                raise ValueError(
                    f"Unexpected protein chain {chain!r} at residue "
                    f"{residue_number}"
                )

            if (
                residue_name == "LEU"
                and residue_number == 164
                and atom_name == "OXT"
            ):
                removed_terminal_oxt += 1
                continue

            if residue_name == "HIS" and residue_number == 31:
                line = line[:17] + "HID" + line[20:]
                residue_name = "HID"
                changed_residues.add((chain, residue_number))

            output_lines.append(line)
            atom_count += 1
            residue_numbers.append(residue_number)

            if residue_name == "HID" and residue_number == 31:
                hid_atom_count += 1

    if atom_count != 1305:
        raise ValueError(
            f"Expected 1305 retained protein heavy atoms, "
            f"found {atom_count}"
        )

    if removed_terminal_oxt != 1:
        raise ValueError(
            "Expected to remove one LEU164 OXT atom, removed "
            f"{removed_terminal_oxt}"
        )

    if not residue_numbers:
        raise ValueError("No protein atoms were retained")

    if min(residue_numbers) != 1 or max(residue_numbers) != 164:
        raise ValueError(
            "Expected protein residue range 1–164, found "
            f"{min(residue_numbers)}–{max(residue_numbers)}"
        )

    if changed_residues != {("A", 31)}:
        raise ValueError(
            "Expected to rename only chain A HIS31 to HID; changed "
            f"{sorted(changed_residues)}"
        )

    if hid_atom_count != 10:
        raise ValueError(
            f"Expected 10 heavy atoms for HID31, found {hid_atom_count}"
        )

    last_serial = int(output_lines[-1][6:11])
    output_lines.append(
        f"TER   {last_serial + 1:5d}      LEU A 164\n"
    )
    output_lines.append("END\n")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("".join(output_lines))

    print(f"Input: {INPUT.relative_to(PROJECT_ROOT)}")
    print(f"Output: {OUTPUT.relative_to(PROJECT_ROOT)}")
    print(f"Protein heavy atoms retained: {atom_count}")
    print("Residue range: MET1–LEU164")
    print(f"HID31 heavy atoms: {hid_atom_count}")
    print(
        "Terminal OXT atoms removed for TLeap reconstruction: "
        f"{removed_terminal_oxt}"
    )
    print("HETATM records retained: 0")
    print("Hydrogens added: 0")


if __name__ == "__main__":
    main()