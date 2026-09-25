"""Build a residue-level feature table from validated GROMACS outputs."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .xvg import read_xvg


def build_feature_table(rmsf_path: str | Path, sasa_path: str | Path) -> pd.DataFrame:
    """Merge per-residue RMSF and SASA values using residue number."""
    rmsf = read_xvg(rmsf_path, columns=["residue_number", "rmsf_nm"])
    sasa = read_xvg(sasa_path)
    if sasa.shape[1] == 2:
        sasa.columns = ["residue_number", "sasa_nm2"]
    elif sasa.shape[1] == 3:
        sasa.columns = ["residue_number", "sasa_nm2", "sasa_std_nm2"]
    else:
        raise ValueError("SASA input must contain 2 or 3 columns")

    for frame in (rmsf, sasa):
        frame["residue_number"] = frame["residue_number"].astype(int)

    if rmsf["residue_number"].duplicated().any():
        raise ValueError("Duplicate residue numbers in RMSF input")
    if sasa["residue_number"].duplicated().any():
        raise ValueError("Duplicate residue numbers in SASA input")

    merged = rmsf.merge(sasa, on="residue_number", how="outer", validate="one_to_one")
    merged = merged.sort_values("residue_number").reset_index(drop=True)
    if merged[["rmsf_nm", "sasa_nm2"]].isna().any().any():
        missing = merged.loc[merged[["rmsf_nm", "sasa_nm2"]].isna().any(axis=1), "residue_number"]
        raise ValueError(f"RMSF/SASA residue mismatch: {missing.tolist()}")
    return merged


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rmsf", required=True, type=Path)
    parser.add_argument("--sasa", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    features = build_feature_table(args.rmsf, args.sasa)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    features.to_csv(args.output, index=False)
    print(f"Wrote {len(features)} residues to {args.output}")


if __name__ == "__main__":
    main()

