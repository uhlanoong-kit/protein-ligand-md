from pathlib import Path

import pytest

from protein_ligand_md.xvg import read_xvg


def test_read_xvg_ignores_metadata(tmp_path: Path) -> None:
    path = tmp_path / "example.xvg"
    path.write_text("@ title \"Example\"\n# comment\n1 0.10\n2 0.20\n")
    frame = read_xvg(path, columns=["residue", "value"])
    assert frame.to_dict("records") == [
        {"residue": 1.0, "value": 0.10},
        {"residue": 2.0, "value": 0.20},
    ]


def test_read_xvg_rejects_inconsistent_columns(tmp_path: Path) -> None:
    path = tmp_path / "bad.xvg"
    path.write_text("1 0.10\n2 0.20 9\n")
    with pytest.raises(ValueError, match="Inconsistent column count"):
        read_xvg(path)

