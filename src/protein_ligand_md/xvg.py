"""Small, strict parser for two-column and multi-column GROMACS XVG files."""

from pathlib import Path
from typing import Sequence

import pandas as pd


def read_xvg(path: str | Path, columns: Sequence[str] | None = None) -> pd.DataFrame:
    """Read numeric XVG data while ignoring metadata and comment lines."""
    path = Path(path)
    rows: list[list[float]] = []
    for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith(("#", "@")):
            continue
        try:
            rows.append([float(value) for value in line.split()])
        except ValueError as exc:
            raise ValueError(f"Non-numeric XVG data at {path}:{line_number}") from exc

    if not rows:
        raise ValueError(f"No numeric data found in {path}")

    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError(f"Inconsistent column count in {path}")

    if columns is None:
        columns = [f"column_{index + 1}" for index in range(width)]
    if len(columns) != width:
        raise ValueError(f"Expected {len(columns)} columns but found {width} in {path}")

    return pd.DataFrame(rows, columns=list(columns))

