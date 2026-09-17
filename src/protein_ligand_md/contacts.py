"""Calculate per-residue protein-ligand contact occupancy with MDAnalysis."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Iterable

import pandas as pd


def summarize_contacts(
    contacted_resindices: Iterable[Iterable[int]],
    residue_metadata: dict[int, tuple[int, str]],
) -> pd.DataFrame:
    """Convert per-frame contacted residue indices into an occupancy table."""
    frame_contacts = [set(frame) for frame in contacted_resindices]
    if not frame_contacts:
        raise ValueError("No trajectory frames were analyzed")

    counts: Counter[int] = Counter()
    for contacts in frame_contacts:
        counts.update(contacts)

    rows = []
    for resindex, count in sorted(counts.items(), key=lambda item: residue_metadata[item[0]][0]):
        resid, resname = residue_metadata[resindex]
        rows.append(
            {
                "residue_number": resid,
                "residue_name": resname,
                "contact_frames": count,
                "total_frames": len(frame_contacts),
                "contact_occupancy": count / len(frame_contacts),
            }
        )
    return pd.DataFrame(rows)


def calculate_contact_occupancy(
    topology: Path,
    trajectory: Path,
    ligand_selection: str,
    protein_selection: str,
    cutoff_angstrom: float,
) -> pd.DataFrame:
    """Calculate whether each protein residue contacts the ligand per frame."""
    import MDAnalysis as mda
    from MDAnalysis.lib.distances import capped_distance

    universe = mda.Universe(str(topology), str(trajectory))
    protein = universe.select_atoms(protein_selection)
    ligand = universe.select_atoms(ligand_selection)
    if protein.n_atoms == 0:
        raise ValueError(f"Protein selection is empty: {protein_selection}")
    if ligand.n_atoms == 0:
        raise ValueError(f"Ligand selection is empty: {ligand_selection}")

    residue_metadata = {
        int(residue.resindex): (int(residue.resid), str(residue.resname))
        for residue in protein.residues
    }
    contacts_by_frame: list[set[int]] = []
    for _ in universe.trajectory:
        pairs = capped_distance(
            protein.positions,
            ligand.positions,
            max_cutoff=cutoff_angstrom,
            box=universe.dimensions,
            return_distances=False,
        )
        contacts_by_frame.append(set(int(x) for x in protein.resindices[pairs[:, 0]]))

    return summarize_contacts(contacts_by_frame, residue_metadata)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topology", required=True, type=Path)
    parser.add_argument("--trajectory", required=True, type=Path)
    parser.add_argument("--ligand", required=True, help='MDAnalysis selection, e.g. "resname BNZ"')
    parser.add_argument("--protein", default="protein", help="MDAnalysis protein selection")
    parser.add_argument("--cutoff", default=4.0, type=float, help="Contact cutoff in angstrom")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    table = calculate_contact_occupancy(
        args.topology,
        args.trajectory,
        args.ligand,
        args.protein,
        args.cutoff,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(args.output, index=False)
    print(f"Wrote {len(table)} contacting residues to {args.output}")


if __name__ == "__main__":
    main()

