#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "${script_dir}/.." && pwd)"

input="${project_root}/data/processed/BNZ_complete.mol2"
work_dir="${project_root}/data/processed/bnz_parameterization"
verified_dir="${project_root}/parameters/bnz"

for program in python antechamber parmchk2 tleap; do
    if ! command -v "${program}" >/dev/null 2>&1; then
        echo "Required program not found: ${program}" >&2
        exit 1
    fi
done

python "${project_root}/scripts/04_prepare_bnz.py"

mkdir -p "${work_dir}"
cd "${work_dir}"

antechamber \
    -i "${input}" \
    -fi mol2 \
    -o BNZ_gaff2.mol2 \
    -fo mol2 \
    -at gaff2 \
    -c bcc \
    -nc 0 \
    -rn BNZ \
    -s 2

parmchk2 \
    -i BNZ_gaff2.mol2 \
    -f mol2 \
    -o BNZ_gaff2.frcmod \
    -s gaff2

tleap \
    -f "${verified_dir}/BNZ_tleap.in" \
    > BNZ_tleap.log 2>&1

grep -q \
    "Exiting LEaP: Errors = 0; Warnings = 0; Notes = 0." \
    BNZ_tleap.log

python - <<'PY'
from collections import Counter

import parmed as pmd


structure = pmd.load_file(
    "BNZ_gaff2.prmtop",
    "BNZ_gaff2.inpcrd",
)

atom_types = Counter(atom.type for atom in structure.atoms)
total_charge = sum(atom.charge for atom in structure.atoms)

assert len(structure.atoms) == 12
assert len(structure.residues) == 1
assert len(structure.bonds) == 12
assert atom_types == Counter({"ca": 6, "ha": 6})
assert abs(total_charge) < 1.0e-6

print("Atoms:", len(structure.atoms))
print("Residues:", len(structure.residues))
print("Bonds:", len(structure.bonds))
print("Atom types:", atom_types)
print("Total charge:", f"{total_charge:.6f}")
PY

cmp BNZ_gaff2.mol2 "${verified_dir}/BNZ_gaff2.mol2"
cmp BNZ_gaff2.frcmod "${verified_dir}/BNZ_gaff2.frcmod"

echo "BNZ parameterization reproduced successfully."