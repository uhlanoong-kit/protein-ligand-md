from pathlib import Path

import pytest

from protein_ligand_md.features import build_feature_table


def test_build_feature_table(tmp_path: Path) -> None:
    rmsf = tmp_path / "rmsf.xvg"
    sasa = tmp_path / "sasa.xvg"
    rmsf.write_text("1 0.10\n2 0.20\n")
    sasa.write_text("1 1.50\n2 2.50\n")

    frame = build_feature_table(rmsf, sasa)
    assert frame.columns.tolist() == ["residue_number", "rmsf_nm", "sasa_nm2"]
    assert frame["residue_number"].tolist() == [1, 2]
    assert frame["sasa_nm2"].tolist() == [1.5, 2.5]


def test_build_feature_table_rejects_residue_mismatch(tmp_path: Path) -> None:
    rmsf = tmp_path / "rmsf.xvg"
    sasa = tmp_path / "sasa.xvg"
    rmsf.write_text("1 0.10\n2 0.20\n")
    sasa.write_text("1 1.50\n3 2.50\n")

    with pytest.raises(ValueError, match="residue mismatch"):
        build_feature_table(rmsf, sasa)

