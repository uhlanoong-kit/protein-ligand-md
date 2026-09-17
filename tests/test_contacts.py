import pytest

from protein_ligand_md.contacts import summarize_contacts


def test_summarize_contacts_counts_unique_frames() -> None:
    frame_contacts = [{10, 11}, {10}, {11}, set()]
    metadata = {10: (100, "LEU"), 11: (101, "VAL")}
    table = summarize_contacts(frame_contacts, metadata)

    assert table["residue_number"].tolist() == [100, 101]
    assert table["contact_frames"].tolist() == [2, 2]
    assert table["contact_occupancy"].tolist() == [0.5, 0.5]


def test_summarize_contacts_requires_frames() -> None:
    with pytest.raises(ValueError, match="No trajectory frames"):
        summarize_contacts([], {})

