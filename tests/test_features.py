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



def test_build_feature_table_with_sasa_std(tmp_path: Path) -> None:
    rmsf = tmp_path / "rmsf.xvg"
    sasa = tmp_path / "sasa.xvg"
    rmsf.write_text("1 0.10\n2 0.20\n")
    sasa.write_text(
        "# SASA mean and standard deviation\n"
        "2 2.50 0.30\n"
        "1 1.50 0.20\n"
    )

    frame = build_feature_table(rmsf, sasa)

    assert frame.columns.tolist() == [
        "residue_number", "rmsf_nm", "sasa_nm2", "sasa_std_nm2"
    ]
    assert frame["residue_number"].tolist() == [1, 2]
    assert frame["sasa_nm2"].tolist() == [1.5, 2.5]
    assert frame["sasa_std_nm2"].tolist() == [0.2, 0.3]


@pytest.mark.parametrize("row", ["1", "1 1.50 0.20 9.0"])
def test_build_feature_table_rejects_sasa_width(tmp_path: Path, row: str) -> None:
    rmsf = tmp_path / "rmsf.xvg"
    sasa = tmp_path / "sasa.xvg"
    rmsf.write_text("1 0.10\n")
    sasa.write_text(row + "\n")

    with pytest.raises(ValueError, match="SASA input must contain 2 or 3 columns"):
        build_feature_table(rmsf, sasa)
